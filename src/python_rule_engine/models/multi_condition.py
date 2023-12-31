from __future__ import annotations

from typing import List, Optional

from .condition import Condition
from .simple_condition import SimpleCondition


class MultiCondition(Condition):
    def __init__(self, **data) -> None:
        super().__init__()

        if sum([bool(data.get("any", [])), bool(data.get("all", [])), bool(data.get("not", {}))]) != 1:
            raise ValueError("Only one of any, all or not can be defined")

        self.all = self.__validate_conditions(data.get("all", []), data["operators_dict"])
        self.any = self.__validate_conditions(data.get("any", []), data["operators_dict"])
        self.not_ = self.__validate_not_condition(data.get("not", {}), data["operators_dict"])

    def __validate_conditions(self, data: List[dict], operators_dict) -> Optional[List[Condition]]:
        if not data:
            return None
        cds = []
        for cd in data:
            cd["operators_dict"] = operators_dict
            try:
                cds.append(SimpleCondition(**cd))
            except ValueError:
                cds.append(MultiCondition(**cd))
        return cds

    def __validate_not_condition(self, data: dict, operators_dict) -> Optional[Condition]:
        if not data:
            return None
        data["operators_dict"] = operators_dict
        try:
            return SimpleCondition(**data)
        except ValueError:
            return MultiCondition(**data)

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
