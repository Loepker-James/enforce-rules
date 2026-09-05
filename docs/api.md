# validate(value, rules)

This is the main function of the library. I will list what each keyword does, allowed types, and version it was created in (if I didn't specify one, 
then 1.0.0 is default).

Value: The value being validated
Rules: The rules for validation

## Supported Rules Dictionaries:

### length:

Allowed types: anything that has a length

Parameter: integer length

Example: ```{"length": 5}```

### min_length:

Allowed types: anything that has a length

Parameter: integer length

Example: ```{"min_length": 3}```

### max_length:

Allowed types: anything that has a length

Parameter: integer length

Example: ```{"max_length": 7}```

### min:

Allowed types: float or int

Parameter: a number

Example: ```{"min": 0}```

### max:

Allowed types: float or int

Parameter: a number

Example: ```{"max": 10}```

### allowed_values:

Allowed types: All

Parameter: A list of any python objects.

Example: ```{"allowed_values": ("a", "b", "c", "d")}```

### invariant:

Allowed types: bool

Parameter: A boolean stating whether or not the condition should activate

Example: ```{"invariant": True}```

### all_same:

Allowed types: List/tuple/set (preferribly)

Parameter: A boolean stating whether or not the condition should activate

Example: ```{"all_same": True}```

### all_unique:

Allowed types: List/tuple/set (preferribly)

Parameter: A boolean stating whether or not the condition should activate

Example: ```{"all_same": True}```

### non_empty:

Allowed types: Anything with a length

Parameter: a boolean stating whether or not the condition should activate

Example: ```{"non_empty": True}```

### no_nulls:

Allowed types: Any collection

Parameter: a boolean stating whether or not the condition should activate

Example: ```{"no_nulls": True}```

### sorted:

Allowed types: List/tuple/set (preferribly)

Parameter: A boolean stating whether or not the condition should activate

Example: ```{"sorted": True}```

### increasing:

Allowed types: List/tuple/set (preferribly)

Parameter: A boolean stating whether or not the condition should activate

Example: ```{"increasing": True}```

### decreasing:

Allowed types: List/tuple/set (preferribly)

Parameter: A boolean stating whether or not the condition should activate

Example: ```{"decreasing": True}```

### sum_min:

Allowed types: Anything with a sum

Parameter: A number

Example: ```{"sum_min": 0}```

### sum_max:

Allowed types: Anything with a sum

Parameter: A number

Example: ```{"sum_max": 100}```

### element_min:

Allowed types: Any collection of numbers

Parameter: A number

Example: ```{"element_min": 0}```

### element_max:

Allowed types: Any collection of numbers

Parameter: A number

Example: ```{"element_max": 50}```

### regex:

Allowed types: string

Parameter: The regex pattern (string)

Example: ```{"regex": "abc"}```

### regex_flags:

Allowed types: All (this goes along with regex though, which requires a string)

Parameter: The regex flags

Example: ```python
import re
{"regex": "abc", "regex_flags": re.I | re.M | re.X}```

### must_be_true:

Allowed types: Any

Parameter: A function whose signature is ```Callable[[object], bool]```.

Example: ```{"must_be_true": lambda x: x % 2 == 0}```

### before_date (Created in 2.0.0):

Allowed types: datetime object

Parameter: a datetime object

Example: ```python
from datetime import datetime
{"before_date": datetime(2000, 1, 1)}```

### after_date (Created in 2.0.0):

Allowed types: datetime object

Parameter: a datetime object

Example: ```python
from datetime import datetime
{"after_date": datetime(2000, 1, 1)}```

### piece_color (Created in 3.0.0):

Allowed types: Piece object

Parameter: chess.WHITE or chess.BLACK

Example: ```python
import chess
{"piece_color": chess.WHITE}```

### piece_type (Created in 3.0.0):
Allowed types: Piece object

Parameter: Chess.PAWN, chess.KNIGHT, chess.BISHOP, chess.ROOK, chess.QUEEN, or chess.KING

Example: ```python
import chess
{"piece_type": chess.KNIGHT}```

### chess_symbol (Created in 3.0.0):

Allowed types: Piece object

Parameter: a string representing the piece's symbol

Example: ```{"chess_symbol": "r"})```

### is_password (Created in 3.1.0):

Allowed types: string

Parameter: a boolean stating whether or not the condition will activate

Example: ```{"is_password": True}```
