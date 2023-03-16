from python_rule_engine.models import SimpleCondition
from python_rule_engine.operators import Operator


def test_custom_operator():
    class EqualLowercase(Operator):
        id = "equal_lowercase"

        @staticmethod
        def match(condition, obj_value, run_condition):
            return condition.value.lower() == obj_value.lower(), obj_value

    assert EqualLowercase.match(SimpleCondition(value="Santiago", operator="equal_lowercase"), "SANTIAGO", None) == (True, "SANTIAGO")
