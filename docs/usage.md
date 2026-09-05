Usage Guide
This guide explains how to use Project Enforce Rules in simple steps. It shows how to install the library, how to call the validate function, and how rule dictionaries work.

Installation
Install the library using pip:

```bash
pip install enforce-rules
```

Basic Usage
The main function in this library is validate(value, rules_dict).
You pass in a value and a dictionary describing the rules you want to enforce.

Example:

```python
validate(10, {"min": 0})
```
This checks that the value is at least 0.

Using Multiple Rules
You can enforce several rules at once by adding more keys to the dictionary.

```python
validate(75, {"min": 0, "max": 100})
```

This ensures the value is between 0 and 100.

String Rules
Rules also work with strings. For example, you can enforce minimum length:

```python
validate("cat", {"min_length": 3})
```

Regex Rule
The regex rule checks whether a pattern appears in the value.
Version 1.1+ uses re.search instead of re.fullmatch.

```python
validate("xabc", {"regex": "abc"})
```

This passes (in version 1.1+) because "abc" appears anywhere in the string.

What Happens When Validation Fails
If the value does not meet the rules, validate raises a ValueError.
This prevents invalid data from silently passing through your program.

Example:

```python
validate(-5, {"min": 0})
```

This raises an error because -5 does not satisfy the minimum rule.
