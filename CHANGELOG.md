# Changelog

All notable changes to this project will be documented in this file.



## 1.0.0 - Created on 8/22/2026



### Added

* validate() function
* Keywords:



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

numbers = validate(\[1, 1, 1], {"all_same": True})

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

my_things = validate([1, 2, 3, "a", "b", "c"], {"no\_nulls": True})

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





must_be_true

Custom rule: a function that returns True for allowed values.



```python

def is_even(x: int) -> bool:
    return x % 2 == 0

even_number = validate(8, {"must\_be\_true": is\_even})

```

This calls:



```python

is_even(8)

```

### Documentation

* Added full keyword reference table to README
* Clarified behavior of `must_be_true`
* Added examples for all keywords
* Updated installation instructions
* Added Versioning Policy section in README


## 1.0.1 - Created on 8/29/2026

### Refactored
* Type hints no longer use Any and use object instead.
* Fixed inconsistency in readme

## 1.0.2 - Created on 8/29/2026

### Refactored
* Made newlines more visible for the readme on PyPI.



