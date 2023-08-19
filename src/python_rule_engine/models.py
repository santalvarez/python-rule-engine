from __future__ import annotations
from abc import ABC
from typing import List, Any, Union, Optional
from pydantic import BaseModel, root_validator, validator

from .json_path import JSONPath


class Condition(BaseModel, ABC):
    match: bool = False

class SimpleCondition(Condition):
    operator: str
    params: dict = {}
    value: Any
    path: Optional[JSONPath] = None
    match_detail: Any = None

    # pylint: disable=no-self-argument,no-self-use
    @validator('path', pre=True)
    def create_json_path(cls, value: str):
        return JSONPath(value)

    class Config:
        arbitrary_types_allowed = True

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
    description: str = None
    extra: dict = None
    conditions: MultiCondition

SimpleCondition.update_forward_refs()
