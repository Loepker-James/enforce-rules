# Design Document

## Purpose of This Document
This document explains the internal architecture of the library, the reasoning behind major design decisions, and how rule validation is structured. It is not a tutorial or API reference. Instead, it describes why the system works the way it does and how maintainers should understand its design.

## High‑Level Goals
The project focuses on simplicity, predictable behavior, and dictionary‑based rule definitions. All validation occurs at runtime, allowing rules to be added, removed, or modified without changing application code.

Key goals:

* predictable rule behavior
* explicit control flow
* easy extension
* minimal abstraction
* no hidden logic

The system avoids complex metadata objects or class hierarchies. Instead, it uses a flexible rule dictionary and explicit dispatch logic.

## Overall Architecture
The library consists of three main components:

### Validator
The `validate()` function is the central entry point. It receives:

* a value
* a dictionary of rules

It loops through each rule and dispatches to the correct helper using `match/case`. Unknown rule names raise an error immediately.

### Rule Functions
Each rule is implemented as a helper function named:

```python
_validate_rule_name
```

These helpers are pure, isolated, and responsible for raising `ValueError` on failure.

### Helper Utilities
Utilities support:

* regex compilation
* type normalization
* error formatting
* datetime comparison
* chess‑specific logic

## Rule Dictionary Design Philosophy
The `ValidateDict` type is not a strict schema. It is a flexible “rule bag” used for pattern matching. Each key corresponds to a rule. Every key is optional. Different validations use different subsets. This flexibility is intentional.

## Why It Is Not a Schema
Large TypedDicts are often criticized when used as configuration objects. However, `ValidateDict` is not a configuration model — it is a dispatch table. TypedDict is used for documentation, autocomplete, and static analysis, not enforcement.

Validators normalize types internally (for example, `int(rule)`), so strict typing is unnecessary.

## Why match/case Is Used
Python’s structural pattern matching is ideal for rule dispatch:

* explicit rule handling
* predictable control flow
* easy extension
* readable logic
* partial dict matching

Example:

```python
match key:
    case "min":
        _validate_min(value, rule)
    ...
    case "regex":
        _validate_regex(value, str(rule), rules.get("regex_flags"))
```


## Convenience Wrapper (Version 3.2)
Version 3.2 introduces `is_valid()`, a boolean wrapper around `validate()`:

```python
def is_valid(value: object, rules: Dict[str, object]) -> bool:
    try:
        validate(value, rules)
        return True
    except:
        return False
```


This wrapper does not modify rule logic. It simply converts exceptions into boolean results.

## Rule Categories
Rules are grouped by behavior:

### Length‑Based Rules
Operate on values with `len()`.  
Examples: `length`, `min_length`, `max_length`, `non_empty`.

### Numeric Rules
Operate on numbers or numeric aggregates.  
Examples: `min`, `max`, `sum_min`, `sum_max`, `element_min`, `element_max`.

### Collection Rules
Operate on iterables.  
Examples: `all_same`, `all_unique`, `no_nulls`, `sorted`, `increasing`, `decreasing`.

### Membership Rules
Check membership.  
Example: `allowed_values`.

### Boolean Activation Rules
Enabled only when their parameter is True.  
Examples: `invariant`, `is_password`.

### Regex Rules
Pattern matching using `re.search`.  
Examples: `regex`, `regex_flags`.

### Datetime Rules
Chronological comparisons.  
Examples: `before_date`, `after_date`.

### Chess‑Specific Rules
Operate on python‑chess pieces.  
Examples: `piece_color`, `piece_type`, `chess_symbol`.

### Custom Callable Rules
User‑defined logic.  
Example: `must_be_true`.

## Rule Mapping
Rule names map directly to helper functions: ```validate_rule_name```

Example:
```python
validate(20, {"min": 10})
```

calls

```python
_validate_min(20, 10)
```


## Validator Design
The validator loops through each rule:

```python
for key, rule in rules.items():
    match key:
...
        case "min":
            _validate_min(value, rule)
...
```


Unknown keys raise: ```ValueError(f"Unknown rule: {key}")```


### Early Exit
Validation stops at the first failure because exceptions propagate immediately.

### Error Strategy
All failures raise `ValueError`. Messages vary by rule to provide context.

## Regex Design
Starting in version 1.1.0, the validator switched from `re.fullmatch` to `re.search` to allow more flexible patterns.

## Datetime Rule Design
Version 2.0.0 introduced `before_date` and `after_date`.

Examples:

```python
validate(datetime(1999, 8, 29), {"before_date": datetime(2000, 1, 1)})
validate(datetime(2001, 8, 29), {"after_date": datetime(2000, 1, 1)})
```


## Chess Rule Design
Version 3.0.0 added chess rules:

* `piece_color` → `piece.color == rule_value`
* `piece_type` → `piece.piece_type == rule_value`
* `chess_symbol` → `piece.symbol() == rule_value`

## Password Rule Design
Version 3.1.0 added `is_password`, enforcing:

1. length ≥ 8
2. ≥ 1 digit
3. ≥ 1 uppercase
4. ≥ 1 lowercase
5. ≥ 1 symbol

Failures raise `ValueError`.

## Custom Callable Rule
`must_be_true` allows arbitrary validation:

```python
U = TypeVar("U")
def _validate_must_be_true(value: U, func: Callable[[U], bool]) -> None:
    if not func(value):
        raise ValueError("must_be_true rule failed")
```


## Extensibility
New rules can be added by:

* opening an issue
* demonstrating common usage
* adding a new `_validate_<rule>` helper
* adding a new `case "<rule>"` entry

The system is intentionally easy to extend.

## Design Tradeoffs
The project uses dictionary‑based rules because:

* metadata objects add complexity
* class hierarchies are unnecessary
* dynamic rule sets are easier to express
* match/case dispatch is explicit and predictable

## Future Plans
Planned improvements:

* better error messages
* more rule categories
* performance optimizations
* potential plugin support
