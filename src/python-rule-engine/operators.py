from typing import Callable, Tuple, Any
from abc import ABC, abstractmethod
from .models import SimpleCondition

class Operator(ABC):
    @property
    @abstractmethod
    def id(self) -> str:
        pass

    @abstractmethod
    def match(self, condition: SimpleCondition, obj_value, run_condition: Callable[..., SimpleCondition]) -> Tuple[bool, Any]:
        pass

class Equal(Operator):
    id = "equal"

    def match(self, condition, obj_value, run_condition) -> Tuple[bool, Any]:
        """ Return True if both values match"""
        return condition.value == obj_value, obj_value
