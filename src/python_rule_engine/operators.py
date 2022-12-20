from typing import Callable, Tuple, Any
from abc import ABC, abstractmethod
from .models import SimpleCondition

class Operator(ABC):
    @property
    @abstractmethod
    def id(self) -> str:
        pass

    @staticmethod
    @abstractmethod
    def match(condition: SimpleCondition, obj_value, run_condition: Callable[..., SimpleCondition]) -> Tuple[bool, Any]:
        """ Evaluate the condition on the object. This will be called by the rule engine.

        :param SimpleCondition condition: The condition to evaluate the object on
        :param Any obj_value: The object to evaluate
        :param Callable[..., SimpleCondition] run_condition: A callable in case the condition value
            is a condition itself.
        :return Tuple[bool, Any]: The result of the evaluation and details about the evaluation.
            Usually the details is the obejct itself. But in other cases it can also
            be a subset of the object.
        """

class Equal(Operator):
    id = "equal"

    @staticmethod
    def match(condition, obj_value, run_condition) -> Tuple[bool, Any]:
        """ Return True if both values match"""
        return condition.value == obj_value, obj_value
