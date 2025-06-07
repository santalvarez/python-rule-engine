from typing import Any, Dict, List, Optional

from .models.rule import Rule
from .operators import Operator
from .decoder import RuleDecoder


class RuleEngine:
    def __init__(self, rules: List[Dict], operators: Optional[List[Operator]] = None):
        self.decoder = RuleDecoder(operators)
        self.rules = self.decoder.decode_rules(rules)

    def add_rule(self, rule: Dict):
        """ Add a rule to the engine

        :param Dict rule: The rule to add
        """
        self.rules.append(self.decoder.decode_rule(rule))

    def add_str_rule(self, rule: str):
        """ Add a rule to the engine

        :param str rule: The rule to add
        """
        self.rules.append(self.decoder.decode_str_rule(rule))

    def remove_rule(self, rule_name: str):
        """ Remove a rule from the engine

        :param str rule_name: The name of the rule to remove
        """
        self.rules = [rule for rule in self.rules if rule.name != rule_name]

    def evaluate(self, obj: Any) -> List[Rule]:
        """ Evaluate an object on the loaded rules

        :param Any obj: The object to evaluate.
        :return List[Rule]: The list of rules that match the object
        """
        results = []
        for rule in self.rules:
            rule_copy = rule.model_copy(deep=True)
            rule_copy.conditions.evaluate(obj)

            if rule_copy.conditions.match:
                results.append(rule_copy)

        return results
