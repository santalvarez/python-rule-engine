import json
from json import JSONDecodeError
from typing import Any, Dict, List, Optional, Type

from pydantic import ValidationError

from .errors import (DuplicateOperatorError, InvalidRuleJSONError,
                     InvalidRuleSchemaError, InvalidRuleTypeError)
from .models.rule import Rule
from .operators import DEFAULT_OPERATORS, Operator


class RuleDecoder:
    """ Class responsible for decoding rules """
    def __init__(self, custom_operators: Optional[List[Type[Operator]]]=None):
        self.operators = {}

        if custom_operators is None: custom_operators = []

        for p in DEFAULT_OPERATORS + custom_operators:
            if p.id in self.operators:
                raise DuplicateOperatorError
            self.operators[p.id] = p


    def decode_rules(self, rules: List[Dict]) -> List[Rule]:
        """ Decodes a list of rule dictionaries into a list of Rule objects """
        return [self.decode_rule(rule) for rule in rules]

    def decode_rule(self, rule: Dict) -> Rule:
        """ Decodes a rule dictionary into a Rule object """
        if not isinstance(rule, dict):
            raise InvalidRuleTypeError
        try:
            return Rule(**rule, operators_dict=self.operators)
        except Exception as e:
            raise InvalidRuleSchemaError from e

    def decode_str_rules(self, rules: List[str]) -> List[Rule]:
        """ Decodes a list of rule strings into a list of Rule objects """
        return [self.decode_str_rule(rule) for rule in rules]

    def decode_str_rule(self, rule: str) -> Rule:
        """ Decodes a rule string into a Rule object """
        if not isinstance(rule, str):
            raise InvalidRuleTypeError
        try:
            rule_dict = json.loads(rule)
            return Rule(**rule_dict, operators_dict=self.operators)
        except (JSONDecodeError, ValidationError) as e:
            raise InvalidRuleSchemaError from e
