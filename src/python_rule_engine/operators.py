from abc import ABC, abstractmethod
from typing import Any, Tuple, List, Type


class Operator(ABC):
    @property
    @abstractmethod
    def id(self) -> str:
        pass

    def __init__(self, condition):
        self.condition = condition

    @abstractmethod
    def match(self, obj_value) -> Tuple[bool, Any]:
        """ Evaluate the condition on the object. This will be called by the rule engine.

        :param Any obj_value: The object to evaluate
        :return Tuple[bool, Any]: The result of the evaluation and details about the evaluation.
            Usually the details is the obejct itself. But in other cases it can also
            be a subset of the object.
        """

class Equal(Operator):
    id = "equal"

    def match(self, obj_value) -> Tuple[bool, Any]:
        """ Return True if both values match"""
        return self.condition.value == obj_value, obj_value

class NotEqual(Operator):
    id = "not_equal"

    def match(self, obj_value) -> Tuple[bool, Any]:
        """ Return True if both values do not match"""
        return self.condition.value != obj_value, obj_value

class LessThan(Operator):
    id = "less_than"

    def match(self, obj_value) -> Tuple[bool, Any]:
        """ Return True if the object value is less than the condition value"""
        return obj_value < self.condition.value, obj_value

class LessThanInclusive(Operator):
    id = "less_than_inclusive"

    def match(self, obj_value) -> Tuple[bool, Any]:
        """ Return True if the object value is less than or equal to the condition value"""
        return obj_value <= self.condition.value, obj_value

class GreaterThan(Operator):
    id = "greater_than"

    def match(self, obj_value) -> Tuple[bool, Any]:
        """ Return True if the object value is greater than the condition value"""
        return obj_value > self.condition.value, obj_value

class GreaterThanInclusive(Operator):
    id = "greater_than_inclusive"

    def match(self, obj_value) -> Tuple[bool, Any]:
        """ Return True if the object value is greater than or equal to the condition value"""
        return obj_value >= self.condition.value, obj_value

class In(Operator):
    id = "in"

    def match(self, obj_value) -> Tuple[bool, Any]:
        """ Return True if the object value is in the condition value"""
        return obj_value in self.condition.value, obj_value

class NotIn(Operator):
    id = "not_in"

    def match(self, obj_value) -> Tuple[bool, Any]:
        """ Return True if the object value is not in the condition value"""
        return obj_value not in self.condition.value, obj_value

class Contains(Operator):
    id = "contains"

    def match(self, obj_value) -> Tuple[bool, Any]:
        """ Return True if the object value contains the condition value"""
        return self.condition.value in obj_value, obj_value

class NotContains(Operator):
    id = "not_contains"

    def match(self, obj_value) -> Tuple[bool, Any]:
        """ Return True if the object value does not contain the condition value"""
        return self.condition.value not in obj_value, obj_value


DEFAULT_OPERATORS: List[Type[Operator]] = [
    Equal, NotEqual, LessThan, LessThanInclusive, GreaterThan,
    GreaterThanInclusive, In, NotIn, Contains, NotContains]
