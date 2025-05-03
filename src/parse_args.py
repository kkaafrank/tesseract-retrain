import argparse

from src.game_script_parsing import InputTypes


def parse_command_line_args(argv: list[str]) -> argparse.Namespace:
    """Parses passed in command line arguments

    Args:
        argv (list[str]): command line arguments, without the first arg (path to executed file)

    Returns:
        argparse.Namespace: Namespace object containing argument properties
    """
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "--input",
        required=True,
    )
    parser.add_argument(
        "--input_format",
        choices=InputTypes.get_input_options(),
        default=InputTypes.EXCEL.value,
    )

    args = parser.parse_args(argv)
    return args
