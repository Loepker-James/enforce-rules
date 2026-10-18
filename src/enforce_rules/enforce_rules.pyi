from collections.abc import Iterable
from datetime import datetime
from typing import Any, Callable, Literal, TypedDict, TypeVar, Annotated
from pydantic import Field

_T = TypeVar("_T")
Number = int | float
LengthType = int

T = object() #Ignore this

class ValidateDict(TypedDict, total=False):
    length: LengthType
    min_length: LengthType
    max_length: LengthType
    min: Number
    max: Number
    allowed_values: Iterable[object]
    invariant: bool
    all_same: bool
    all_unique: bool
    non_empty: bool
    no_nulls: bool
    sorted: bool
    increasing: bool
    decreasing: bool
    sum_min: Number
    sum_max: Number
    element_min: Number
    element_max: Number
    regex: str
    regex_flags: object
    must_be_true: Callable[[Any], bool]
    before_date: datetime
    after_date: datetime
    piece_color: bool
    piece_type: Literal[1, 2, 3, 4, 5, 6]
    chess_symbol: Literal["p", "n", "b", "r", "q", "k", "P", "N", "B", "R", "Q", "K"]
    is_password: bool

def validate(value: _T, rules: ValidateDict) -> _T: ...
def is_valid(value: _T, rules: ValidateDict) -> bool: ...
def compile_rules(rules: ValidateDict) -> Callable[[_T], _T]: ...
