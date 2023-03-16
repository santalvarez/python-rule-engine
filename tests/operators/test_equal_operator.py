from python_rule_engine.models import SimpleCondition
from python_rule_engine.operators import Equal


def test_equal_operator():
    condition1 = SimpleCondition(value="Santiago", operator="equal")
    condition2 = SimpleCondition(value=12345, operator="equal")
    condition3 = SimpleCondition(value=True, operator="equal")

    assert Equal.match(condition1, "Santiago", None) == (True, "Santiago")
    assert Equal.match(condition1, "Not Santiago", None) == (False, "Not Santiago")

    assert Equal.match(condition2, 12345, None) == (True, 12345)
    assert Equal.match(condition2, 12346, None) == (False, 12346)

    assert Equal.match(condition3, True, None) == (True, True)
    assert Equal.match(condition3, False, None) == (False, False)
