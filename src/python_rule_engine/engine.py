from copy import deepcopy
from typing import Any, Dict, List, Optional, Type

from .exceptions import DuplicateOperatorError
from .models.rule import Rule
from .operators import (Contains, Equal, GreaterThan, GreaterThanInclusive, In,
                        LessThan, LessThanInclusive, NotContains, NotEqual,
                        NotIn, Operator)


class RuleEngine:
    default_operators: List[Type[Operator]] = [Equal, NotEqual, LessThan,
                                               LessThanInclusive, GreaterThan, GreaterThanInclusive,
                                               In, NotIn, Contains, NotContains]

    def __init__(self, rules: List[Dict], operators: Optional[List[Operator]] = None):
        self.operators: Dict[str, Type[Operator]] = self._merge_operators(operators)
        self.rules = self._deserialize_rules(rules)

    def _merge_operators(self, operators: Optional[List[Type[Operator]]] = None) -> Dict[str, Type[Operator]]:
        merged_operators = {}

        if operators is None:
            operators = []
        for p in self.default_operators + operators:
            if p.id in merged_operators:
                raise DuplicateOperatorError
            merged_operators[p.id] = p
        return merged_operators

    def _deserialize_rules(self, rules: List[Dict]) -> List[Rule]:
        aux_rules = []
        for rule in rules:
            aux_rules.append(Rule(rule, self.operators))
        return aux_rules

    def evaluate(self, obj: Any) -> List[Rule]:
        """ Evaluate an object on the loaded rules

        :param Any obj: The object to evaluate.
        :return List[Rule]: The list of rules that match the object
        """
        results = []
        for rule in self.rules:
            rule_copy = deepcopy(rule)
            rule_copy.conditions.evaluate(obj)

            if rule_copy.conditions.match:
                results.append(rule_copy)

        return results
