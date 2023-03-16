from python_rule_engine.models import SimpleCondition
from python_rule_engine.operators import In


def test_in_operator():
    condition1 = SimpleCondition(value=[1, 2, 3], operator="in")
    condition2 = SimpleCondition(value=["Santiago", "Alvarez"], operator="in")
    condition3 = SimpleCondition(value=[True, False], operator="in")

    assert In.match(condition1, 1, None) == (True, 1)
    assert In.match(condition1, 4, None) == (False, 4)

    assert In.match(condition2, "Santiago", None) == (True, "Santiago")
    assert In.match(condition2, "Zapata", None) == (False, "Zapata")

    assert In.match(condition3, True, None) == (True, True)
    assert In.match(condition3, None, None) == (False, None)
