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

class NotEqual(Operator):
    id = "not_equal"

    @staticmethod
    def match(condition, obj_value, run_condition) -> Tuple[bool, Any]:
        """ Return True if both values do not match"""
        return condition.value != obj_value, obj_value

class LessThan(Operator):
    id = "less_than"

    @staticmethod
    def match(condition, obj_value, run_condition) -> Tuple[bool, Any]:
        """ Return True if the object value is less than the condition value"""
        return obj_value < condition.value, obj_value

class LessThanInclusive(Operator):
    id = "less_than_inclusive"

    @staticmethod
    def match(condition, obj_value, run_condition) -> Tuple[bool, Any]:
        """ Return True if the object value is less than or equal to the condition value"""
        return obj_value <= condition.value, obj_value

class GreaterThan(Operator):
    id = "greater_than"

    @staticmethod
    def match(condition, obj_value, run_condition) -> Tuple[bool, Any]:
        """ Return True if the object value is greater than the condition value"""
        return obj_value > condition.value, obj_value

class GreaterThanInclusive(Operator):
    id = "greater_than_inclusive"

    @staticmethod
    def match(condition, obj_value, run_condition) -> Tuple[bool, Any]:
        """ Return True if the object value is greater than or equal to the condition value"""
        return obj_value >= condition.value, obj_value

class In(Operator):
    id = "in"

    @staticmethod
    def match(condition, obj_value, run_condition) -> Tuple[bool, Any]:
        """ Return True if the object value is in the condition value"""
        return obj_value in condition.value, obj_value

class NotIn(Operator):
    id = "not_in"

    @staticmethod
    def match(condition, obj_value, run_condition) -> Tuple[bool, Any]:
        """ Return True if the object value is not in the condition value"""
        return obj_value not in condition.value, obj_value

class Contains(Operator):
    id = "contains"

    @staticmethod
    def match(condition, obj_value, run_condition) -> Tuple[bool, Any]:
        """ Return True if the object value contains the condition value"""
        return condition.value in obj_value, obj_value

class NotContains(Operator):
    id = "not_contains"

    @staticmethod
    def match(condition, obj_value, run_condition) -> Tuple[bool, Any]:
        """ Return True if the object value does not contain the condition value"""
        return condition.value not in obj_value, obj_value
