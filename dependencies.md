# Dependencies

This project requires the following Python modules to run:

# Built-in modules (no installation required)
* ```typing```
* ```collections.abc```
* ```re```
* ```datetime```

These are included with all standard Python installations.

# External modules (installation required)
* ```python-chess``` (1.11+)
* ```pydantic``` (2+)

Download the raw [```requirements.txt```](https://github.com/Loepker-James/enforce-rules/blob/main/requirements.txt) file, then install dependencies by giving pip the full path to the file:

```bash
python -m pip install -r /path/to/requirements.txt
```


# Notes
* ```python-chess``` is required only for the ```chess.Piece``` type hint used in the code.
* ```pydantic``` is required only for the ```PositiveInt``` type hint.

# Test Dependencies

These modules are required only for running the test suite:

# Built-in test modules (no installation required)
* ```unittest```
* ```typing```
* ```re```

# External test modules (installation required)
* ```enforce-rules``` (newest verseion)

Install test dependencies with:

```bash
python -m pip install enforce-rules
```

# Test Notes
* ```unittest``` is used to structure and run the test cases.
* ```typing``` is used for type annotations inside test files.
* ```re``` is used for regex validation in test assertions.
* ```enforce-rules``` is required because the test suite imports the main project.
