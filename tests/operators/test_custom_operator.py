from python_rule_engine.models.simple_condition import SimpleCondition
from python_rule_engine.operators import Operator


def test_custom_operator(operators_dict):
    class EqualLowercase(Operator):
        id = "equal_lowercase"

        def match(self, obj_value):
            return self.condition.value.lower() == obj_value.lower(), obj_value

    operators_dict[EqualLowercase.id] = EqualLowercase
    condition = SimpleCondition(value="Santiago", operator="equal_lowercase",
                                operators_dict=operators_dict)

    condition.evaluate("Santiago")
    assert (condition.match, condition.match_detail) == (True, "Santiago")
