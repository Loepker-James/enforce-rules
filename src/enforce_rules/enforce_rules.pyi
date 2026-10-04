from typing import TypeVar, Dict
from collections.abc import Sequence, Iterable

T = TypeVar("T")

def validate(value: T, rules: Dict[str, object]) -> T: ...
def is_valid(value: T, rules: Dict[str, object]) -> T: ...
