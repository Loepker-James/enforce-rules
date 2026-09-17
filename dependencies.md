# Dependencies

This project requires the following Python modules to run:

## Built-in modules (no installation required)
- typing
- collections.abc
- re
- datetime

These are included with all standard Python installations.

## External modules (installation required)
- python-chess
- pydantic

Install them with:

    python -m pip install python-chess pydantic

## Notes
- `python-chess` is required for board logic, move validation, and piece utilities.
- `pydantic` is required for model validation, constrained types (e.g., PositiveInt), and structured configuration.
