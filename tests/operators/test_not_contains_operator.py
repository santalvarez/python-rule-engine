from python_rule_engine.models import SimpleCondition
from python_rule_engine.operators import NotContains


def test_not_contains_operator():
    condition1 = SimpleCondition(value=1, operator="not_contains")
    condition2 = SimpleCondition(value="Santiago", operator="not_contains")
    condition3 = SimpleCondition(value=True, operator="not_contains")

    assert NotContains.match(condition1, [1, 2, 3], None) == (False, [1,2,3])
    assert NotContains.match(condition1, [2, 3, 4], None) == (True, [2,3,4])

    assert NotContains.match(condition2, ["Santiago", "Alvarez"], None) == (False, ["Santiago", "Alvarez"])
    assert NotContains.match(condition2, ["Zapata", "Alvarez"], None) == (True, ["Zapata", "Alvarez"])

    assert NotContains.match(condition3, [True, True], None) == (False, [True, True])
    assert NotContains.match(condition3, [False, False], None) == (True, [False, False])
