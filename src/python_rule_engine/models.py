from __future__ import annotations
from abc import ABC
from typing import List, Any, Union
from pydantic import BaseModel, root_validator, validator


class Condition(BaseModel, ABC):
    match: bool = False

class SimpleCondition(Condition):
    operator: str
    params: dict = {}
    value: Any
    path: str = None
    match_detail: Any = None

    # pylint: disable=no-self-argument,no-self-use
    @validator("path")
    def validate_path(cls, value):
        if value[:2] != "$.":
            raise ValueError("Invalid Definition: First two chars of 'path' have to be $.")
        return value

class MultiCondition(Condition):
    all: List[Union[SimpleCondition, MultiCondition]] = None
    any: List[Union[SimpleCondition, MultiCondition]] = None

    # pylint: disable=no-self-argument,no-self-use
    @root_validator
    def validate_one_is_present(cls, values):
        if values['all'] and values['any']:
            raise ValueError("Only one operator is supported")
        if not values['all'] and not values['any']:
            raise ValueError("No valid operators found")
        return values

class Rule(BaseModel):
    name: str
    conditions: MultiCondition

SimpleCondition.update_forward_refs()
