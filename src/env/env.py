from pathlib import Path

from dotenv import dotenv_values

_PARENT_FOLDER = Path(__file__).parent

ENV = {
    **dotenv_values(_PARENT_FOLDER / "prod.env"),
    **dotenv_values(_PARENT_FOLDER / ".env"),
}
