from __future__ import annotations

from typing import Dict, List, Union

from pydantic import Field, model_validator

from .condition import Condition
from .simple_condition import SimpleCondition


class MultiCondition(Condition):
    any: List[Union[SimpleCondition, MultiCondition]] = None
    all: List[Union[SimpleCondition, MultiCondition]] = None
    not_: Union[SimpleCondition, MultiCondition] = Field(None, alias="not")

    operators_dict: Dict = Field(..., exclude=True)

    @model_validator(mode="after")
    def validate_conditions(self):
        if sum([bool(self.any), bool(self.all), bool(self.not_)]) != 1:
            raise ValueError("Only one of any, all or not can be defined")
        return self

    @model_validator(mode="before")
    @classmethod
    def set_operators_dict(cls, values):
        operators_dict = values["operators_dict"]

        for key in ["any", "all"]:
            if values.get(key):
                for item in values[key]:
                    item["operators_dict"] = operators_dict

        if values.get("not"):
            values["not"]["operators_dict"] = operators_dict

        return values

    def evaluate(self, obj):
        """ Run a multi condition on an object or dict

        :param Any obj: The object
        """

        if self.any:
            return self.evaluate_any(obj)

        if self.all:
            return self.evaluate_all(obj)

        return self.evaluate_not(obj)

    def evaluate_any(self, obj):
        """
        Run a multi condition on a dict with 'any' type.

        :param obj: The object to be tested.
        """

        for _, cond in enumerate(self.any):
            cond.evaluate(obj)

            if cond.match:
                self.match = True
                break

    def evaluate_all(self, obj):
        """
        Run a multi condition on a dict with 'all' type.

        :param obj: The object to be tested.
        """

        for _, cond in enumerate(self.all):
            cond.evaluate(obj)

            if not cond.match:
                self.match = False
                return

        self.match = True

    def evaluate_not(self, obj):
        """
        Run a multi condition on a dict with 'not' type.

        :param obj: The object to be tested.
        """

        self.not_.evaluate(obj)

        self.match = not self.not_.match
