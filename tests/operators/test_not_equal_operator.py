from python_rule_engine.models import SimpleCondition
from python_rule_engine.operators import NotEqual


def test_not_equal_operator():
    condition1 = SimpleCondition(value="Santiago", operator="not_equal")
    condition2 = SimpleCondition(value=12345, operator="not_equal")
    condition3 = SimpleCondition(value=True, operator="not_equal")

    assert NotEqual.match(condition1, "Santiago", None) == (False, "Santiago")
    assert NotEqual.match(condition1, "Not Santiago", None) == (True, "Not Santiago")

    assert NotEqual.match(condition2, 12345, None) == (False, 12345)
    assert NotEqual.match(condition2, 12346, None) == (True, 12346)

    assert NotEqual.match(condition3, True, None) == (False, True)
    assert NotEqual.match(condition3, False, None) == (True, False)
