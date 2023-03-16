from python_rule_engine.models import SimpleCondition
from python_rule_engine.operators import LessThan


def test_less_than_operator():
    condition1 = SimpleCondition(value=10, operator="less_than")
    condition2 = SimpleCondition(value=10.5, operator="less_than")
    condition3 = SimpleCondition(value="Santiago", operator="less_than")

    assert LessThan.match(condition1, 5, None) == (True, 5)
    assert LessThan.match(condition1, 15, None) == (False, 15)

    assert LessThan.match(condition2, 10.4, None) == (True, 10.4)
    assert LessThan.match(condition2, 10.6, None) == (False, 10.6)

    assert LessThan.match(condition3, "Alvarez", None) == (True, "Alvarez")
    assert LessThan.match(condition3, "Zapata", None) == (False, "Zapata")
