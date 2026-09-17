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

```bash
python -m pip install python-chess pydantic
```

## Notes
- ```python-chess``` is required only for the ```chess.Piece``` type hint used in the code.
- ```pydantic``` is required only for the ```PositiveInt``` type hint and other constrained types.
