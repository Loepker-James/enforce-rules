Project Enforce Rules
Project Enforce Rules (or PER for short) expands the Python type system to allow more constraints.

Version #
----------------
MAJOR: 3

MINOR: 0

PATCH: 2

If you need to catch up, you can see the full version history in the [CHANGELOG](https://github.com/Loepker-James/enforce-rules/blob/main/CHANGELOG.md).

It exists to let you use features Python doesn't already provide in the typing system — things you probably want, like min, max, length, all_same, and many more.

PER now supports runtime validation anywhere using:

```python
validate(value: object, rules: Dict[str, Any])
```

This enforces rule dictionaries and returns the original value if valid.
If invalid, it raises a descriptive error.

Why I Made It
I wanted type‑hint features Python didn’t give me. I thought dictionaries would work until I learned... well...
Python didn’t enforce them.

So with the help of Microsoft Copilot and my dad, we designed a module that enforces this type of stuff. 
Then I realized everyone in the Python community could use this, so it became a project. Hence, creating PER.

PER uses rule dictionaries and validate() to enforce constraints at runtime.

Install it with pip:

```bash
pip install enforce-rules
```
Then use it like:

```python
from enforce_rules import validate
```
Features
1. Runtime enforcement of rule dictionaries
2. Dictionary‑based rule definitions
3. No extra objects required
4. Works anywhere in your code
5. Extensible via must_be_true

How It Works
PER validates values using:

```python
validate(value, rules)
```
If the value violates a rule, PER raises an error.
If the value passes, PER returns the original value unchanged.

This means validated values behave exactly like normal Python values.

Keywords and Usage
Below are all supported keywords.

length

The length of the object must be exactly this.

```python
lst = validate([1, 2, 3, 4, 5], {"length": 5})
```

min_length

Minimum length (inclusive).

```python
lst = validate(['a', 'b', 'c', 'd', 'e'], {"min_length": 3})
```
max_length

Maximum length (inclusive).

```python
lst = validate([1, 2, 3, 4, 5, 6], {"max_length": 7})
```
min

Minimum numeric value (inclusive).

```python
number = validate(10, {"min": 0})
```
max

Maximum numeric value (inclusive).

```python
number = validate(10, {"max": 20})
```
allowed_values

Similar to Literal; value must be one of the allowed values.

```python
val = validate("a", {"allowed_values": ("a", "b", "c", "d")})
```
invariant

Value must be truthy.

```python
val = validate((0 == 0), {"invariant": True})
```
all_same

All values in the collection must be the same.

```python
numbers = validate([1, 1, 1], {"all_same": True})
```
all_unique

All values in the collection must be unique.

```python
numbers = validate([1, 2, 3], {"all_unique": True})
```
non_empty

Collection must not be empty.

```python
my_strings = validate(['a', 'b', 'c'], {"non_empty": True})
```
no_nulls

Collection must not contain None.

```python
my_things = validate([1, 2, 3, "a", "b", "c"], {"no_nulls": True})
```

sorted

List must be sorted (increasing or decreasing).

```python
numbers = validate([1, 5, 9], {"sorted": True})
```

increasing

List must be strictly increasing.

```python
numbers = validate([1, 5, 9], {"increasing": True})
```
decreasing

List must be strictly decreasing.

```python
numbers = validate([9, 5, 1], {"decreasing": True})
```
sum_min

Minimum sum of the collection (inclusive).

```python
numbers = validate([10, 20, 30], {"sum_min": 50})
```
sum_max

Maximum sum of the collection (inclusive).

```python
numbers = validate([10, 20, 30], {"sum_max": 70})
```
element_min

Minimum value for any element (inclusive).

```python
numbers = validate([10, 20, 30], {"element_min": 5})
```
element_max

Maximum value for any element (inclusive).

```python
numbers = validate([10, 20, 30], {"element_max": 40})
```
regex

String must match the regex.

```python
cat_or_dog = validate("cat", {"regex": "cat|dog"})
```
regex_flags 

Turns out I didn't notice this in my code, until 1.1.0. This is the regex flags

```python
from re import RegexFlag
cat_or_dog = validate("cat", {"regex": "cat|dog", {"regex_flags": RegexFlag.I | RegexFlag.M | RegexFlag.X
```
before_date

Value must be strictly before the given datetime.

```python
validate(datetime(1999, 8, 29), {"before_date": datetime(2000, 1, 1)})
```

after_date

Value must be strictly after the given datetime.
```python
validate(datetime(2026, 8, 29), {"after_date": datetime(2000, 1, 1)})
```

piece_color

The piece must have this exact color (True for white, False for black).

```python
import chess
piece = validate(chess.Piece(chess.ROOK, chess.WHITE), {"piece_color": chess.WHITE})
```
piece_type

The piece must be exactly this type (e.g., chess.KNIGHT, chess.ROOK).

```python
import chess
piece = validate(chess.Piece(chess.KNIGHT, chess.WHITE), {"piece_type": chess.KNIGHT})
```
chess_symbol

The piece’s symbol must match this string ("P", "n", "r", etc.).

```python
import chess
piece = validate(chess.Piece(chess.ROOK, chess.BLACK), {"chess_symbol": "r"})
```

must_be_true

Custom rule: a function that returns True for allowed values.

```python
def is_even(x: int) -> bool:
    return x % 2 == 0
even_number = validate(8, {"must_be_true": is_even})
```
This calls:

```python
is_even(8)
```
If enough people use a must_be_true lambda, it may become an added keyword in a later version

Contributing
Contributions are welcome. Please open an issue or pull request.
When contributing, ensure backwards compatibility (you cannot remove keywords and/or features).

Please note, when using my module, that you will manually have to validate each time should you choose to mutate a variable.


Versioning Policy
-----------------

This project guarantees full backwards compatibility. Existing rule files, keyword meanings, validator behaviors, and metadata formats will continue to work exactly as before. No update will ever break existing configurations.

Version Numbering
-----------------
This project uses a non-breaking semantic versioning model:

MAJOR.MINOR.PATCH

MAJOR = large new feature families
MINOR = small additive keywords or enhancements
PATCH = bug fixes or internal improvements

Major bumps do not imply breaking changes. They only indicate that a significant new capability has been added.

Major bumps always reset MINOR and PATCH to 0. For example:
1.7.3 -> 2.0.0

1.12.0 -> 2.0.0

1.0.0 -> 2.0.0

Minor bumps always reset PATCH to 0. For example:
1.7.3 -> 1.8.0

1.12.9 -> 1.13.0

1.0.4 -> 1.1.0

Minor Version Bumps
-------------------
Minor bumps occur when adding small keywords. Examples include:

min_inclusive

max_inclusive

trim_whitespace

pattern_flags

These additions do not change the meaning of existing keywords, do not require users to modify rule files, and do not alter validator behavior. They are classified as minor updates.

Minor bumps always reset PATCH to 0



Credits
Microsoft Copilot — for helping me code it. It did a TON of the coding, and to be honest, I couldn't have made this project without it. It did ~~some~~ a lot of readme, in addition to it writing most of CONTRIBUTING.md
Dad — for helping me along the journey.

License Type: BSD 3-clause
