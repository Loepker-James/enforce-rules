# `validate(value, rules)`

This is the main function of the library. I will list what each keyword does, allowed types, and version it was created in (if I didn't specify one, 
then 1.0.0 is default).

Value: The value being validated

Rules: The rules for validation

## Supported Rules Dictionaries:

### length:

Allowed types: anything that has a length

Parameter: integer length

Example: `validate("abcde", {"length": 5})`

### min_length:

Allowed types: anything that has a length

Parameter: integer length

Example: `validate("abcde", {"min_length": 3})`

### max_length:

Allowed types: anything that has a length

Parameter: integer length

Example: `validate("abcde", {"max_length": 7})`

### min:

Allowed types: a number

Parameter: a number

Example: `validate(5, {"min": 0})`

### max:

Allowed types: float or int

Parameter: a number

Example: `validate(5, {"max": 10})`

### allowed_values:

Allowed types: All

Parameter: A list of any python objects.

Example: `validate("b", {"allowed_values": ("a", "b", "c", "d")})`

### invariant:

Allowed types: bool

Parameter: A boolean stating whether or not the condition should activate

Example: `validate(True, {"invariant": True})`

### all_same:

Allowed types: List/tuple/set (preferribly)

Parameter: A boolean stating whether or not the condition should activate

Example: `validate([1, 1, 1, 1, 1], {"all_same": True})`

### all_unique:

Allowed types: List/tuple/set (preferribly)

Parameter: A boolean stating whether or not the condition should activate

Example: `validate([1, 3, 6, 10, 15], {"all_unique": True})`

### non_empty:

Allowed types: Anything with a length

Parameter: a boolean stating whether or not the condition should activate

Example: `validate(["a", "b", "c"], {"non_empty": True})`

### no_nulls:

Allowed types: Any collection

Parameter: a boolean stating whether or not the condition should activate

Example: `validate([1, "a", 2, "b", 3, "c"], {"no_nulls": True})`

### sorted:

Allowed types: A Sequence

Parameter: A boolean stating whether or not the condition should activate

Example: `validate([10, 20, 30, 40, 50], {"sorted": True})`

### increasing:

Allowed types: A Sequence

Parameter: A boolean stating whether or not the condition should activate

Example: `validate([10, 20, 30, 40, 50], {"increasing": True})`

### decreasing:

Allowed types: A Sequence

Parameter: A boolean stating whether or not the condition should activate

Example: `validate([50, 40, 30, 20, 10], {"decreasing": True})`

### sum_min:

Allowed types: Anything with a sum

Parameter: A number

Example: `validate([10, -5], {"sum_min": 0})`

### sum_max:

Allowed types: Anything with a sum

Parameter: A number

Example: `validate([10, 20, 50], {"sum_max": 100})`

### element_min:

Allowed types: Any collection of numbers

Parameter: A number

Example: `validate([1, 2, 3], {"element_min": 0})`

### element_max:

Allowed types: Any collection of numbers

Parameter: A number

Example: `validate([10, 20, 30, 40, 45], {"element_max": 50})`

### regex:

Allowed types: string

Parameter: The regex pattern (string)

Example: `validate("abc", {"regex": "^abc$"})`

### regex_flags:

Allowed types: All (this goes along with regex though, which requires a string)

Parameter: The regex flags

Example: 
```python
import re
validate("aBc", {"regex": "abc", "regex_flags": re.I})
```

### must_be_true:

Allowed types: Any

Parameter: A function whose signature is `Callable[[object], bool]`.

Example: `validate(8, {"must_be_true": lambda x: x % 2 == 0})`

### before_date (Created in 2.0.0):

Allowed types: datetime object

Parameter: a datetime object

Example: 
```python
from datetime import datetime
validate(datetime(1999, 8, 29), {"before_date": datetime(2000, 1, 1)})
```

### after_date (Created in 2.0.0):

Allowed types: datetime object

Parameter: a datetime object

Example: 
```python
from datetime import datetime
validate(datetime(2001, 8, 29), {"after_date": datetime(2000, 1, 1)})
```

### piece_color (Created in 3.0.0):

Allowed types: Piece object

Parameter: chess.WHITE or chess.BLACK

Example: 
```python
import chess
validate(chess.Piece(chess.PAWN, chess.WHITE), {"piece_color": chess.WHITE})
```

### piece_type (Created in 3.0.0):
Allowed types: Piece object

Parameter: Chess.PAWN, chess.KNIGHT, chess.BISHOP, chess.ROOK, chess.QUEEN, or chess.KING

Example: 
```python
import chess
validate(chess.Piece(chess.KNIGHT, chess.BLACK), {"piece_type": chess.KNIGHT})
```

### chess_symbol (Created in 3.0.0):

Allowed types: Piece object

Parameter: a string representing the piece's symbol

Example: 
```python
import chess
validate(chess.Piece(chess.ROOK, chess.BLACK), {"chess_symbol": "r"})
```

### is_password (Created in 3.1.0):

Allowed types: string

Parameter: a boolean stating whether or not the condition will activate

Example: `validate("A6(dEfGhI", {"is_password": True})`



# `is_valid(value, rules)` (created in 3.2.0)
`is_valid` is a helper added in version 3.2.0. It wraps `validate()` and answers yes or no instead of raising an error.

```python
from enforce_rules import is_valid

is_valid(10, {"min": 0})   # True
is_valid(-1, {"min": 0})   # False
```

It returns `True` when every rule passes and `False` when anything goes wrong while checking, including a failed rule, a value of the wrong type, or a misspelled rule name. Use `validate()` to find out why. It adds no rule logic of its own, and it is for people who prefer a boolean to catching exceptions.

The current source is in [`enforce_rules.py`](src/enforce_rules/enforce_rules.py), where you can search for `def is_valid`.
