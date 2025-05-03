import sys
from pathlib import Path

from src import game_script_parsing, parse_args


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

    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
