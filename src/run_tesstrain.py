from src import constants
from src.env.env import ENV

TRAINED_DATA_SUFFIX = ".traineddata"
TRAINING_RATIO = 0.8


# TODO: figure out why this wont run in windows pwsh from subprocess
#   works fine in bash manually
def create_tesstrain_bash_script() -> None:
    """Creates a bash script that will run the tesseract training."""
    tessdata_path = constants.REPO_ROOT / "tessdata_best"
    tesstrain_path = constants.REPO_ROOT / "tesstrain"

    command_parts = [
        "make",
        "training",
        f"MODEL_NAME={ENV['MODEL_NAME']}",
        f"START_MODEL={ENV['TARGET_LANG']}",
        f"TESSDATA={tessdata_path.as_posix()}",
        f"RATIO_TRAIN={TRAINING_RATIO}",
    ]

    command_file_path = constants.REPO_ROOT / "data" / "make_training.sh"
    command = " ".join(command_parts)
    script_lines = "\n".join(
        [
            "#!/bin/bash",
            f"cd {tesstrain_path.as_posix()}",
            command,
        ]
    )

    with open(
        command_file_path, "w", encoding="utf-8", newline="\n"
    ) as train_script_file:
        train_script_file.write(script_lines)


# TODO call created bash script
