import os
import subprocess
from pathlib import Path
from shutil import rmtree

from src import constants, game_script_parsing
from src.env.env import ENV

OUTPUT_RESOLUTION = 1500
OUTPUT_FONT_SIZE = 15
DATA_FOLDER = constants.REPO_ROOT / "data"
UNICHARSET_SUFFIX = "unicharset"


def extract_unicode_character_set(target_language: str) -> Path | None:
    """Extracts the base language's unicode character set

    Args:
        target_language (str): the base language, must match with an existing file in the tessdata repo

    Returns:
        Path | None: The path to the extracted unicode character set file.
            None if the target language does not exist or the desired unicharset file was not found.
    """
    target_traineddata = constants.REPO_ROOT / "tessdata_best" / target_language
    target_traineddata = target_traineddata.with_suffix(".traineddata")
    output_dir = DATA_FOLDER / "unpacked_traineddata"
    output_stub = output_dir / f"{target_language}."

    if output_stub.parent.exists():
        rmtree(output_stub.parent)
    os.makedirs(output_stub.parent, exist_ok=True)

    if not target_traineddata.exists():
        return None

    subprocess_args = [
        "combine_tessdata",
        "-u",
        target_traineddata,
        str(output_stub),
    ]
    subprocess.run(subprocess_args, check=True)

    unpacked_files = os.listdir(output_dir)
    for file_name in unpacked_files:
        if UNICHARSET_SUFFIX not in file_name:
            continue

        return output_dir / file_name

    return None


def generate_image_files(parent_folder: Path, unicode_character_set_path: Path) -> bool:
    """Generates image files (.box and .tif) for each text file in parent_folder using
    the font specified in the config

    Args:
        parent_folder (Path): folder containing all text files
        unicode_character_set_path (Path): the extract unicharset file from the target language

    Returns:
        bool: if all image files were successfully generated
    """
    text_files = parent_folder.glob(game_script_parsing.OUTPUT_TEXT_NAME_GLOB)

    for num_files, input_text_file in enumerate(text_files):
        output_file_stub = game_script_parsing.OUTPUT_FILE_BASE.format(num_files)

        try:
            subprocess.run(
                [
                    "text2image",
                    "--text",
                    str(input_text_file),
                    "--outputbase",
                    output_file_stub,
                    "--font",
                    ENV["FONT_NAME"],
                    "--resolution",
                    str(OUTPUT_RESOLUTION),
                    "--ptsize",
                    str(OUTPUT_FONT_SIZE),
                    "--unicharset_file",
                    str(unicode_character_set_path),
                ],
                check=True,
                cwd=parent_folder,
            )
        except Exception as e:
            print(
                f"text2image command encountered an error on {input_text_file}: ",
                e,
            )
            return False

    return True
