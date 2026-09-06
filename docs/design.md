# Design Document

## Purpose of This Document
This is where you will get to learn the design behind the document. Why major decisions were made and many more

## High-Level Goals
Describe the main goals of the project, such as simplicity, predictable behavior, dictionary-based rule definitions, and runtime validation.
Mention that the design prioritizes clarity and ease of extension.

## Overall Architecture
Explain the top-level structure of the library.
Describe how the validator, rule functions, and helper utilities are organized.
Mention how rule keywords map to internal functions.

### Rule Categories
The rule system is organized into categories based on the type of check each rule performs. Categorizing rules makes the validator easier to understand, easier to maintain, and easier to extend. Each category groups rules that operate on similar kinds of data or enforce similar constraints.

* Length-Based Rules  
  These rules operate on any value that has a length. They rely on the built-in len() function and enforce constraints related to size.  
  Examples include: length, min_length, max_length, non_empty.  
  These rules are grouped together because they all measure or require a specific length property.

* Numeric Rules  
  These rules operate on integers or floats. They enforce minimums, maximums, or numeric boundaries on values or collections.  
  Examples include: min, max, sum_min, sum_max, element_min, element_max.  
  They are grouped together because they all involve numeric comparison or numeric aggregation.

* Collection Rules  
  These rules operate on lists, tuples, sets, or any iterable. They inspect multiple elements and often compare them to each other.  
  Examples include: all_same, all_unique, no_nulls, sorted, increasing, decreasing.  
  They form a category because they validate relationships between elements rather than the value itself.

* Membership Rules  
  These rules check whether a value belongs to a predefined set of allowed options.  
  Example: allowed_values.  
  This category exists because membership checks are conceptually different from numeric or structural checks.

* Boolean Activation Rules  
  These rules activate only when their parameter is True. They behave like toggles that enable additional validation logic.  
  Examples include: invariant, is_password.  
  They are grouped together because their behavior depends entirely on a boolean flag.

* Regex Rules  
  These rules operate on strings using regular expressions. They validate patterns and allow optional flags to modify matching behavior.  
  Examples include: regex, regex_flags.  
  They form a category because they rely on Python’s regex engine and pattern matching semantics.

* Datetime Rules  
  These rules operate on datetime objects and enforce temporal ordering.  
  Examples include: before_date, after_date.  
  They are grouped together because they compare chronological relationships rather than numeric or structural ones.

* Chess-Specific Rules  
  These rules operate on python-chess Piece objects and validate chess-specific attributes.  
  Examples include: piece_color, piece_type, chess_symbol.  
  They form a category because they rely on external library types and domain-specific logic.

* Custom Callable Rules  
  These rules allow user-defined validation logic through a function.  
  Example: must_be_true.  
  This category exists to support arbitrary validation conditions that do not fit into any other category.

Categorizing rules in this way ensures that similar rules behave consistently, makes the validator easier to extend with new rule types, and helps users understand which rules apply to which kinds of data. New categories can be added in future versions as the rule system expands.


### Rule Mapping
The validator looks up rule logic by calling

```python
_validate_keyword_name(value, rule_value) #rule_value might be type coerced.
```

when you write

```python
validate(value, {"keyword_name": rule_value})
```


## Validator Design
Explain how validate(value, rules_dict) is structured internally.
The rules loop over in a ```match/case``` loop. Then, calls the appropriate helper whose name is ```_validate_keyword_name```.
If the helper fails, an [early exit](https://github.com/Loepker-James/enforce-rules/blob/main/docs/design.md#early-exit) is triggered. Else, it returns the value put in.

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
Made in version 3.1.0, is_password checks to see if the value is a strong password. ([See Password Issue](https://github.com/Loepker-James/enforce-rules/issues/1)

## Enforcement

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
