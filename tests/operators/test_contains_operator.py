from python_rule_engine.models import SimpleCondition
from python_rule_engine.operators import Contains


def test_contains_operator():
    condition1 = SimpleCondition(value=1, operator="not_contains")
    condition2 = SimpleCondition(value="Santiago", operator="not_contains")
    condition3 = SimpleCondition(value=True, operator="not_contains")

    assert Contains.match(condition1, [1, 2, 3], None) == (True, [1,2,3])
    assert Contains.match(condition1, [2, 3, 4], None) == (False, [2,3,4])

    assert Contains.match(condition2, ["Santiago", "Alvarez"], None) == (True, ["Santiago", "Alvarez"])
    assert Contains.match(condition2, ["Zapata", "Alvarez"], None) == (False, ["Zapata", "Alvarez"])

    assert Contains.match(condition3, [True, True], None) == (True, [True, True])
    assert Contains.match(condition3, [False, False], None) == (False, [False, False])
