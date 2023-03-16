from python_rule_engine.models import SimpleCondition
from python_rule_engine.operators import LessThanInclusive


def test_less_than_inclusive_operator():
    condition1 = SimpleCondition(value=10, operator="less_than_inclusive")
    condition2 = SimpleCondition(value=10.5, operator="less_than_inclusive")
    condition3 = SimpleCondition(value="Santiago", operator="less_than_inclusive")

    assert LessThanInclusive.match(condition1, 5, None) == (True, 5)
    assert LessThanInclusive.match(condition1, 15, None) == (False, 15)
    assert LessThanInclusive.match(condition1, 10, None) == (True, 10)

    assert LessThanInclusive.match(condition2, 10.4, None) == (True, 10.4)
    assert LessThanInclusive.match(condition2, 10.6, None) == (False, 10.6)
    assert LessThanInclusive.match(condition2, 10.5, None) == (True, 10.5)

    assert LessThanInclusive.match(condition3, "Alvarez", None) == (True, "Alvarez")
    assert LessThanInclusive.match(condition3, "Zapata", None) == (False, "Zapata")
    assert LessThanInclusive.match(condition3, "Santiago", None) == (True, "Santiago")
