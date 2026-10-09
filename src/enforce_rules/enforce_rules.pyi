from typing import TypeVar, Dict, TypedDict, Callable, Literal
from collections.abc import Iterable
from datetime import datetime

_T = TypeVar("_T")

class _ValidateDict(TypedDict, total=False):
    length: int
    min_length: int
    max_length: int
    min: int | float
    max: int | float
    allowed_values: Iterable
    invariant: bool
    all_same: bool
    all_unique: bool
    non_empty: bool
    no_nulls: bool
    sorted: bool
    increasing: bool
    decreasing: bool
    sum_min: int | float
    sum_max: int | float
    element_min: int | float
    element_max: int | float
    regex: str
    regex_flags: object
    must_be_true: Callable[[_T], bool]
    before_date: datetime
    after_date: datetime
    piece_color: bool
    piece_type: Literal[1, 2, 3, 4, 5, 6]
    chess_symbol: Literal["p", "n", "b", "r", "q", "k", "P", "N", "B", "R", "Q", "K"]
    is_password: bool

def validate(value: _T, rules: _ValidateDict) -> _T: ...
def is_valid(value: _T, rules: _ValidateDict) -> _T: ...
