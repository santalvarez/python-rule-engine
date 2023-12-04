from __future__ import annotations

from typing import List, Optional

from .condition import Condition
from .simple_condition import SimpleCondition


class MultiCondition(Condition):
    def __init__(self, **data) -> None:
        super().__init__()
        if "all" in data and "any" in data:
            raise ValueError("Only one operator is supported")
        if "all" not in data and "any" not in data:
            raise ValueError("No valid operators found")
        self.all = self.__validate_conditions(data.get("all", []), data["operators_dict"])
        self.any = self.__validate_conditions(data.get("any", []), data["operators_dict"])

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

    def evaluate(self, obj):
        """ Run a multi condition on an object or dict

        :param MultiCondition rule: The rule
        :param Any obj: The object
        :return Rule: The original rule with aded result info
        """

        if self.any:
            return self.evaluate_any(obj)

        return self.evaluate_all(obj)

    def evaluate_any(self, obj):
        """
        Run a multi condition on an object or dict with 'any' type.

        :param multi_condition: The multi condition to be run.
        :param obj: The object to be tested.
        :return: The original multi condition with added result info.
        """

        for _, cond in enumerate(self.any):
            cond.evaluate(obj)

            if cond.match:
                self.match = True
                break

    def evaluate_all(self, obj):
        """
        Run a multi condition on an object or dict with 'all' type.

        :param multi_condition: The multi condition to be run.
        :param obj: The object to be tested.
        :return: The original multi condition with added result info.
        """

        for _, cond in enumerate(self.all):
            cond.evaluate(obj)

            if not cond.match:
                self.match = False
                return

        self.match = True
