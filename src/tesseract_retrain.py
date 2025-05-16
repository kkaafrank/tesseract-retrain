import sys
from pathlib import Path

from src import game_script_parsing, generate_training_images, parse_args, run_tesstrain
from src.env.env import ENV


def main(argv: list[str]) -> int:
    args = parse_args.parse_command_line_args(argv)

    input_path = Path(args.input)
    if not input_path.exists():
        print("Input file not found")
        return 1

    input_type = game_script_parsing.InputTypes(args.input_format)

    text_files_folder = game_script_parsing.extract_japanese_text(
        input_path, input_type
    )

    unicharset_path = generate_training_images.extract_unicode_character_set(
        ENV["TARGET_LANG"]
    )
    if unicharset_path is None:
        print("Unable to unpack unicharset file")
        return 1

    image_gen_success = generate_training_images.generate_image_files(
        text_files_folder, unicharset_path
    )
    if not image_gen_success:
        print("Training image gneneration encountered an error")
        return 1

    if ENV["INVERT_TRAINING_IMAGES"]:
        inversion_success = generate_training_images.invert_images(text_files_folder)
        if not inversion_success:
            print("Error inverting images")
            return 1

    run_tesstrain.create_tesstrain_bash_script()

    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
