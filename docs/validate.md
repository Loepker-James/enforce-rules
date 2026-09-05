```validate()``` checks a value against a set of rules.

Rule dictionaries work by writing a keyword, then a rule value attached to it. For more information look in [api.md](https://github.com/Loepker-James/enforce-rules/blob/main/docs/api.md).

The validator does these steps for each rule.

1. Puts your key in a match/case loop.
2. Calls the corresponding helper with rule value and the value to be validated
3. The helper may raise an error.
4. If none of the helpers raise errors, return the value.

## Keywords:

### length

Checks that the value’s length is exactly equal to the given number.
Failure means the value’s length does not match the required length.

### min_length

Checks that the value’s length is at least the given number.
Failure means the value is too short.

### max_length

Checks that the value’s length is at most the given number.
Failure means the value is too long.

### min

Checks that the numeric value is greater than or equal to the given minimum.
Failure means the value is too small.

### max

Checks that the numeric value is less than or equal to the given maximum.
Failure means the value is too large.

### allowed_values

Checks that the value is one of the allowed options.
Failure means the value is not present in the allowed list or tuple.

### invariant

Checks that the value itself is True when the rule is activated.
Failure means the value is False when invariant=True.

### all_same

Checks that all elements in the collection are identical.
Failure means at least one element differs from the others.

### all_unique

Checks that all elements in the collection are distinct.
Failure means at least one duplicate exists.

### non_empty

Checks that the collection has at least one element.
Failure means the collection is empty.

### no_nulls

Checks that the collection contains no None values.
Failure means at least one element is None.

### sorted

Checks that the collection is sorted in non-decreasing order.
Failure means the collection is not sorted.

### increasing

Checks that each element is strictly greater than the previous one.
Failure means the sequence does not strictly increase.

### decreasing

Checks that each element is strictly less than the previous one.
Failure means the sequence does not strictly decrease.

### sum_min

Checks that the sum of the collection is greater than or equal to the given number.
Failure means the sum is too small.

### sum_max

Checks that the sum of the collection is less than or equal to the given number.
Failure means the sum is too large.

### element_min

Checks that every element in the numeric collection is greater than or equal to the given minimum.
Failure means at least one element is too small.

### element_max

Checks that every element in the numeric collection is less than or equal to the given maximum.
Failure means at least one element is too large.

### regex

Checks that the regex pattern appears somewhere in the string.
Failure means the pattern does not appear anywhere in the value.

### regex_flags

Provides additional flags for the regex rule.
Failure means the pattern does not match even with the provided flags.

### before_date

Checks that the datetime value occurs before the given datetime.
Failure means the value is equal to or after the specified date.

### after_date

Checks that the datetime value occurs after the given datetime.
Failure means the value is equal to or before the specified date.

### piece_color

Checks that the chess piece has the specified color.
Failure means the piece’s color does not match the required one.

### piece_type

Checks that the chess piece has the specified type.
Failure means the piece’s type does not match the required one.

### chess_symbol

Checks that the chess piece’s symbol matches the required string.
Failure means the symbol does not match.

### is_password

Checks that the string meets password requirements when activated.
Failure means the string does not meet one or more password criteria.

### must_be_true

Calls a user-provided function with the value.
Failure means the function returned False.


## Failure Behavior
If any rule fails, the validator raises a ValueError. The exact error message depends on the rule. Some rules include the rule name and the failing value, while others only provide a short message. Validation stops immediately when a rule fails, and no additional rules are checked.
