from python_rule_engine.models import SimpleCondition
from python_rule_engine.operators import NotIn


def test_not_in_operator():
    condition1 = SimpleCondition(value=[1, 2, 3], operator="not_in")
    condition2 = SimpleCondition(value=["Santiago", "Alvarez"], operator="not_in")
    condition3 = SimpleCondition(value=[True, False], operator="not_in")

    assert NotIn.match(condition1, 1, None) == (False, 1)
    assert NotIn.match(condition1, 4, None) == (True, 4)

    assert NotIn.match(condition2, "Santiago", None) == (False, "Santiago")
    assert NotIn.match(condition2, "Zapata", None) == (True, "Zapata")

    assert NotIn.match(condition3, True, None) == (False, True)
    assert NotIn.match(condition3, None, None) == (True, None)
