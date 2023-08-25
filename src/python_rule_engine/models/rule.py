from .multi_condition import MultiCondition
from ..utils import validate_value


class Rule:
    def __init__(self, data, operators_dict):
        self.name = validate_value(data.get("name"), str, "name")
        self.description = validate_value(data.get("description"), str, "description", nullable=True)
        self.extra = validate_value(data.get("extra"), dict, "extra", nullable=True)
        conditions = validate_value(data.get("conditions"), dict, "conditions")
        conditions["operators_dict"] = operators_dict
        self.conditions = MultiCondition(**conditions)

