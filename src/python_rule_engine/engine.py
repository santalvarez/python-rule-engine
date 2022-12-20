from typing import List, Dict, Any
from .operators import (Operator, Equal, NotEqual, LessThan, 
                        LessThanInclusive, GreaterThan, GreaterThanInclusive, 
                        In, NotIn, Contains, NotContains)
from .exceptions import DuplicateOperatorError, OperatorNotFoundError
from .models import Rule, SimpleCondition, MultiCondition

class RuleEngine:
    def __init__(self, rules: List[Dict], operators: List[Operator]=None):
        self.operators: Dict[str, Operator] = self.__merge_operators(operators)
        self.rules = self.__deserialize_rules(rules)

    def __merge_operators(self, operators: List[Operator]=None) -> Dict[str, Operator]:
        merged_operators = {}
        default_operators: List[Operator] = [Equal, NotEqual, LessThan,
                                             LessThanInclusive, GreaterThan, GreaterThanInclusive,
                                             In, NotIn, Contains, NotContains]
        if operators is None:
            operators = []
        for p in default_operators + operators:
            if p.id in merged_operators:
                raise DuplicateOperatorError
            merged_operators[p.id] = p
        return merged_operators

    def __deserialize_rules(self, rules: List[Dict]) -> List[Rule]:
        aux_rules = []
        for rule in rules:
            aux_rules.append(Rule(**rule))
        return aux_rules


    def obj_to_dict(self, obj: Any) -> Any:
        """ Recursively convert an object to a dict if possible

        :param Any obj: The object
        :return Any: The object as a dict or the original object
        """
        if isinstance(obj, dict):
            return {k: self.obj_to_dict(v) for k, v in obj.items()}
        if hasattr(obj, "__dict__"):
            return self.obj_to_dict(obj.__dict__)
        if isinstance(obj, (list, tuple)):
            return [self.obj_to_dict(v) for v in obj]
        return obj

    def get_value_from_jsonpath(self, jsonpath: str, obj: Any) -> Any:
        # TODO: This is a very basic implementation, it should be improved
        # Parse the JSONPath string and extract the attribute names
        attribute_names = jsonpath.replace("$.", "").split(".")

        # Iterate over the attribute names and traverse the object to find the value
        value = obj
        for name in attribute_names:
            if isinstance(value, dict):
                value = value.get(name)
            else:
                value = getattr(value, name)

        return value

    def run_condition(self, condition: SimpleCondition, obj: Any) -> SimpleCondition:
        """ Run a simple condition on an object

        :param Condition condition: The simple condition
        :param Any obj: The object
        :raises OperatorNotFoundError: If a referenced operator is not loaded
        :return condition: The condition with added result info
        """
        operator = condition.operator
        if condition.path:
            path_obj = self.get_value_from_jsonpath(condition.path, obj)
        else:
            path_obj = obj

        try:
            match, match_detail = self.operators[operator].match(
                condition,
                path_obj,
                self.run_condition)
            condition.match = match
            condition.match_detail = self.obj_to_dict(match_detail)
            return condition
        except KeyError as e:
            raise OperatorNotFoundError from e

    def run_multi_condition(self, multi_condition: MultiCondition, obj: Any) -> MultiCondition:
        """ Run a multi condition on an object or dict

        :param MultiCondition rule: The rule
        :param Any obj: The object
        :return Rule: The original rule with aded result info
        """

        if multi_condition.any:
            conditions = multi_condition.any
        else:
            conditions = multi_condition.all

        all_match = True
        for idx, cond in enumerate(conditions):
            # Add if based on type
            if isinstance(cond, SimpleCondition):
                result = self.run_condition(cond, obj)
            else:
                result = self.run_multi_condition(cond, obj)

            conditions[idx] = result

            if multi_condition.any:
                if result.match:
                    multi_condition.match = True
                    break
            else:
                if not result.match:
                    all_match = False
                    break

        if all_match:
            multi_condition.match = True

        if multi_condition.any:
            multi_condition.any = conditions
        else:
            multi_condition.all = conditions

        return multi_condition


    def evaluate(self, obj: Any) -> List[Rule]:
        """ Evaluate an object on the loaded rules

        :param Any obj: The object to evaluate.
        :return List[Rule]: The list of rules that match the object
        """
        results = []
        for rule in self.rules:
            conditions = self.run_multi_condition(rule.conditions, obj)
            if conditions.match:
                rule.conditions = conditions
                results.append(rule)

        return results
