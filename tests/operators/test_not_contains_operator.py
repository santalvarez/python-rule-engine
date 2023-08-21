from python_rule_engine.models.simple_condition import SimpleCondition


def test_not_contains_int(operators_dict):
    condition = SimpleCondition(value=1, operator="not_contains", operators_dict=operators_dict)

    condition.evaluate([1, 2, 3])
    assert (condition.match, condition.match_detail) == (False, [1,2,3])
    condition.evaluate([2, 3, 4])
    assert (condition.match, condition.match_detail) == (True, [2,3,4])

def test_not_contains_str(operators_dict):
    condition = SimpleCondition(value="Santiago", operator="not_contains", operators_dict=operators_dict)

    condition.evaluate("Santiago Alvarez")
    assert (condition.match, condition.match_detail) == (False, "Santiago Alvarez")
    condition.evaluate("Zapata Alvarez")
    assert (condition.match, condition.match_detail) == (True, "Zapata Alvarez")

def test_not_contains_bool(operators_dict):
    condition = SimpleCondition(value=True, operator="not_contains", operators_dict=operators_dict)

    condition.evaluate([True, True])
    assert (condition.match, condition.match_detail) == (False, [True, True])
    condition.evaluate([False, False])
    assert (condition.match, condition.match_detail) == (True, [False, False])
