from python_rule_engine.models import SimpleCondition
from python_rule_engine.operators import GreaterThanInclusive


def test_greater_than_inclusive_operator():
    condition1 = SimpleCondition(value=10, operator="greater_than_inclusive")
    condition2 = SimpleCondition(value=10.5, operator="greater_than_inclusive")
    condition3 = SimpleCondition(value="Santiago", operator="greater_than_inclusive")

    assert GreaterThanInclusive.match(condition1, 5, None) == (False, 5)
    assert GreaterThanInclusive.match(condition1, 15, None) == (True, 15)
    assert GreaterThanInclusive.match(condition1, 10, None) == (True, 10)

    assert GreaterThanInclusive.match(condition2, 10.4, None) == (False, 10.4)
    assert GreaterThanInclusive.match(condition2, 10.6, None) == (True, 10.6)
    assert GreaterThanInclusive.match(condition2, 10.5, None) == (True, 10.5)

    assert GreaterThanInclusive.match(condition3, "Alvarez", None) == (False, "Alvarez")
    assert GreaterThanInclusive.match(condition3, "Zapata", None) == (True, "Zapata")
    assert GreaterThanInclusive.match(condition3, "Santiago", None) == (True, "Santiago")
