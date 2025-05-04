from pathlib import Path

from dotenv import dotenv_values

_PARENT_FOLDER = Path(__file__).parent

ENV = {
    **dotenv_values(_PARENT_FOLDER / "prod.env"),
    **dotenv_values(_PARENT_FOLDER / ".env"),
}

for k, v in ENV.items():
    v_lower = v.lower()
    if v_lower in ("true", "false"):
        ENV[k] = v_lower == "true"
        continue

    try:
        v = float(v)
        if v % 1 == 0:
            v = int(v)

        ENV[k] = v
    except ValueError:
        continue
