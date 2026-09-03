from typing import Dict, Callable, Literal, TypeVar
from collections.abc import Iterable, Sequence, Container
import re
from datetime import datetime
from chess import Piece


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

U = TypeVar("U")
def _validate_must_be_true(value: U, func: Callable[[U], bool]) -> None:
    if not func(value):
        raise ValueError("must_be_true rule failed")

def _validate_before_date(value: datetime, reference: datetime) -> None:
    if not value < reference:
        raise ValueError(f"{value} must be before {reference}.")

def _validate_after_date(value: datetime, reference: datetime) -> None:
    if not value > reference:
        raise ValueError(f"{value} must be before {reference}.")
        
def _validate_piece_color(value: Piece, color: bool) -> None:
    if value.color is not color:
       raise ValueError(f"{value}'s color is {'white' if value.color else 'black'} instead of {'white' if color else 'black'}.")
        
def _validate_piece_type(value: Piece, piece_type: Literal[1, 2, 3, 4, 5, 6]) -> None:
    if value.piece_type != piece_type:
        raise ValueError(f"Value is not a {["pawn", "knight", "bishop", "rook", "queen", "king"][piece_type-1]}")

def _validate_chess_symbol(value: Piece, symbol: Literal["p", "n", "b", "r", "q", "k", "P", "N", "B", "R", "Q", "K"]) -> None:
    if value.symbol() != symbol:
        raise ValueError(f"Value's symbol is not {symbol}")

def _validate_is_password(value: str, rule: bool) -> None:
    if not rule:
        return
    try:
        _validate_min_length(value, 8)
    except ValueError:
        raise ValueError("Password must be at least 8 characters.")
    
    if not any(char.isdigit() for char in value):
        raise ValueError("Password must have at least one digit.")
    
    if not any(char.isupper() for char in value):
        raise ValueError("Password must have at least one uppercase letter.")
    
    if not any(char.islower() for char in value):
        raise ValueError("Password must have at least one lowercase letter.")

    symbols: Container[str] = {
        "!", "\"", "#", "$", "%", "&", "'", "(", ")", "*", "+", ",", "-", ".", "/",
        ":", ";", "<", "=", ">", "?", "@",
        "[", "\\", "]", "^", "_", "`",
        "{", "|", "}", "~",
    }
    
    def is_symbol(char: str) -> bool:
        return char in symbols     
    
    if not any(is_symbol(char) for char in value):
        raise ValueError("Password must have at least one symbol.")

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
            case "piece_color":
                _validate_piece_color(value, bool(rule))
            case "piece_type":
                _validate_piece_type(value, int(rule))
            case "chess_symbol":
                _validate_chess_symbol(value, str(rule))
            case "is_password":
                _validate_is_password(value, rule)
            case "regex_flags":
                # intentionally ignored; handled by regex case
                pass
            case _:
                raise ValueError(f"Unknown rule: {key}")

    return value
