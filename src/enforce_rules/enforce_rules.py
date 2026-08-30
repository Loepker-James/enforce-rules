from typing import Dict, Iterable, Callable, Sequence, Literal, TypeVar
import re
from datetime import datetime


# -----------------------------
# VALIDATOR FUNCTIONS (DEFINED FIRST)
# -----------------------------

def _validate_length(value: Sequence, expected: int) -> None:
    if len(value) != expected:
        raise ValueError(f"Expected length {expected}, got {len(value)}")


def _validate_min_length(value: Sequence, expected: int) -> None:
    if len(value) < expected:
        raise ValueError(f"Expected min length {expected}, got {len(value)}")


def _validate_max_length(value: Sequence, expected: int) -> None:
    if len(value) > expected:
        raise ValueError(f"Expected max length {expected}, got {len(value)}")


def _validate_min(value: float | int, expected: float | int) -> None:
    if value < expected:
        raise ValueError(f"Expected value >= {expected}, got {value}")


def _validate_max(value: float | int, expected: float | int) -> None:
    if value > expected:
        raise ValueError(f"Expected value <= {expected}, got {value}")


def _validate_allowed_values(value: object, allowed: Iterable) -> None:
    if value not in allowed:
        raise ValueError(f"Value {value} not in allowed values {allowed}")


def _validate_invariant(value: object, expected: bool) -> None:
    if expected and not value:
        raise ValueError("Invariant rule failed: value must be truthy")


def _validate_all_same(value: Sequence, expected: bool) -> None:
    if expected and len(set(value)) != 1:
        raise ValueError("All elements must be the same")


def _validate_all_unique(value: Sequence, expected: bool) -> None:
    if expected and len(set(value)) != len(value):
        raise ValueError("All elements must be unique")


def _validate_non_empty(value: Sequence, expected: bool) -> None:
    if expected and len(value) == 0:
        raise ValueError("Collection must not be empty")


def _validate_no_nulls(value: Iterable, expected: bool) -> None:
    if expected and any(v is None for v in value):
        raise ValueError("Collection must not contain None")


def _validate_sorted(value: Sequence, expected: bool) -> None:
    if expected:
        if value != sorted(value) and value != sorted(value, reverse=True):
            raise ValueError("List must be sorted increasing or decreasing")


def _validate_increasing(value: Sequence, expected: bool) -> None:
    if expected:
        for a, b in zip(value, value[1:]):
            if not (b > a):
                raise ValueError("List must be strictly increasing")


def _validate_decreasing(value: Sequence, expected: bool) -> None:
    if expected:
        for a, b in zip(value, value[1:]):
            if not (b < a):
                raise ValueError("List must be strictly decreasing")


def _validate_sum_min(value: Iterable[float | int], expected: float | int) -> None:
    total = sum(value)
    if total < expected:
        raise ValueError(f"Sum must be >= {expected}, got {total}")


def _validate_sum_max(value: Iterable[float | int], expected: float | int) -> None:
    total = sum(value)
    if total > expected:
        raise ValueError(f"Sum must be <= {expected}, got {total}")


def _validate_element_min(value: Iterable[float | int], expected: float | int) -> None:
    if min(value) < expected:
        raise ValueError(f"Elements must be >= {expected}")


def _validate_element_max(value: Iterable[float | int], expected: float | int) -> None:
    if max(value) > expected:
        raise ValueError(f"Elements must be <= {expected}")


def _validate_regex(value: str, pattern: str, flags: object) -> None:
    compiled: re.Pattern = re.compile(pattern, flags or 0)
    if not compiled.search(value):
        raise ValueError(f"Value '{value}' does not match regex '{pattern}'")


def _validate_must_be_true(value: object, func: Callable[[object], bool]) -> None:
    if not func(value):
        raise ValueError("must_be_true rule failed")

def _validate_before_date(value: object, reference: object) -> None:
    if not value < reference:
        raise ValueError(f"{value} must be before {reference}.")

def _validate_after_date(value: object, reference: object) -> None:
    if not value > reference:
        raise ValueError(f"{value} must be before {reference}.")


# -----------------------------
# VALIDATE() — DEFINED LAST
# -----------------------------
T = TypeVar("T")
def validate(value: T, rules: Dict[str, object]) -> T:
    """
    Validate a value against a dictionary of rules.
    Returns the original value if valid, otherwise raises ValueError.
    """
    for key, rule in rules.items():
        match key:
            case "length":
                _validate_length(value, int(rule))
            case "min_length":
                _validate_min_length(value, int(rule))
            case "max_length":
                _validate_max_length(value, int(rule))
            case "min":
                _validate_min(value, rule)
            case "max":
                _validate_max(value, rule)
            case "allowed_values":
                _validate_allowed_values(value, rule)
            case "invariant":
                _validate_invariant(value, bool(rule))
            case "all_same":
                _validate_all_same(value, bool(rule))
            case "all_unique":
                _validate_all_unique(value, bool(rule))
            case "non_empty":
                _validate_non_empty(value, bool(rule))
            case "no_nulls":
                _validate_no_nulls(value, bool(rule))
            case "sorted":
                _validate_sorted(value, bool(rule))
            case "increasing":
                _validate_increasing(value, bool(rule))
            case "decreasing":
                _validate_decreasing(value, bool(rule))
            case "sum_min":
                _validate_sum_min(value, rule)
            case "sum_max":
                _validate_sum_max(value, rule)
            case "element_min":
                _validate_element_min(value, rule)
            case "element_max":
                _validate_element_max(value, rule)
            case "regex":
                _validate_regex(value, str(rule), rules.get("regex_flags"))
            case "must_be_true":
                _validate_must_be_true(value, rule)
            case "before_date":
                _validate_before_date(value, rule)
            case "after_date":
                _validate_after_date(value, rule)
            case x if x != "regex_flags":
                raise ValueError(f"Unknown rule: {key}")

    return value
