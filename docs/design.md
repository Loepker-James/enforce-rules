# Design Document

## Purpose of This Document
Explain that this file describes the internal architecture of the library.
It covers design goals, rule organization, validator structure, and reasoning behind major decisions.
It is not a tutorial or API reference.

## High-Level Goals
Describe the main goals of the project, such as simplicity, predictable behavior, dictionary-based rule definitions, and runtime validation.
Mention that the design prioritizes clarity and ease of extension.

## Overall Architecture
Explain the top-level structure of the library.
Describe how the validator, rule functions, and helper utilities are organized.
Mention how rule keywords map to internal functions.

## Rule System Design
Explain why rules are represented as dictionary keys instead of classes or metadata objects.
Describe how rule parameters are interpreted.
Explain how new rules can be added.

### Rule Mapping
Explain how rule names map to internal functions.
Describe how the validator looks up rule logic.

### Rule Categories
Explain the different categories of rules:
* numeric rules
* length-based rules
* collection-based rules
* regex rules
* datetime rules
* chess-specific rules
* custom callable rules

Describe why they are grouped this way.

## Validator Design
Explain how validate(value, rules_dict) is structured internally.
The rules loop over in a ```match/case``` loop. Then, calls the appropriate helper whose name is ```_validate_keyword_name```.
If the helper fails, an [early exit]() is triggered. Else, it returns the value put in.

### Early Exit
It stops at the first failure because python's errors do that. This is not really intent and more a positive side effect.

### Error Strategy
I use ```ValueError``` for all failures because each failure means the **value** is invalid
Error messages vary by rule due to how I felt like writing it and to give details on the failure.

## Regex Design
Explain the decision to use re.search instead of re.fullmatch.
Describe how this affects rule behavior.
Mention that this change was introduced in version 1.1.

## Datetime Rule Design
before_date and after_date are the datetime made in 2.0.0. For more info, [See Datetime Issue](https://github.com/Loepker-James/enforce-rules/issues/6).
before_date works by ensuring that the value is before rule_value. after_date is similar to before_date but ensures the value is after instead of before. Here is some sample usage:

```python
from datetime import datetime
before_2000 = validate(datetime(1999, 8, 29), {"before_date": datetime(2000, 1, 1)})
```

```python
from datetime import datetime
after_2000 = validate(datetime(2001, 8, 29), {"after_date": datetime(2000, 1, 1)})
```

## Chess Rule Design
Chess rules (made in version 3.0.0, [See Chess Issue](https://github.com/Loepker-James/enforce-rules/issues/7)) were made because I just wanted to expand the domain of my module.
It validates color by ensuring that ```piece.color == color```
It validates type by ensuring that ```piece.piece_type == piece_type```
It validate symbol by ensuring that ```piece.symbol() == symbol```
If a check fails, as you know, a ```ValueError``` is raised.

## Password Rule Design
Made in version 3.1.0, is_password checks to see if the value is a strong password. 

Checks:
1. At least 8 characters
2. At least 1 digit
3. At least 1 uppercase letter
4. At least 1 lowercase letter
5. At least 1 symbol

If any of the checks fail, a ```ValueError``` is raised.

## Custom Callable Rule
must_be_true lets you make your own rules. The rule value you pass in should be ```Callable[[object], bool]```

## Extensibility
New rules can be added if an issue is opened about it and/or many people are using it as a must_be_true rule. Then, the program will do this.

```python
U = TypeVar("U")
def _validate_must_be_true(value: U, func: Callable[[U], bool]) -> None:
    if not func(value):
        raise ValueError("must_be_true rule failed")
```

As you can see, if the function returns a falsy value, a ```ValueError``` is raised. Else, the check passes.

## Design Tradeoffs
I chose dictionary based rules because I didn't want a metadata object. I didn't want complexity. 
I saw no point as to why you can't use metadata objects.

## Future Plans
Here are some things (in addition to issues, that would be great improvements).
* optional type-system integration
* optional plugin support
* improved error messages
* additional rule categories
* performance improvements
