from python_rule_engine.models import SimpleCondition
from python_rule_engine.operators import GreaterThan


def test_greater_than_operator():
    condition1 = SimpleCondition(value=10, operator="greater_than")
    condition2 = SimpleCondition(value=10.5, operator="greater_than")
    condition3 = SimpleCondition(value="Santiago", operator="greater_than")

    assert GreaterThan.match(condition1, 5, None) == (False, 5)
    assert GreaterThan.match(condition1, 15, None) == (True, 15)

    assert GreaterThan.match(condition2, 10.4, None) == (False, 10.4)
    assert GreaterThan.match(condition2, 10.6, None) == (True, 10.6)

    assert GreaterThan.match(condition3, "Alvarez", None) == (False, "Alvarez")
    assert GreaterThan.match(condition3, "Zapata", None) == (True, "Zapata")
