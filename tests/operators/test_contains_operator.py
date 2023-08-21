from python_rule_engine.models.simple_condition import SimpleCondition


def test_contains_operator_int_array(operators_dict):
    condition = SimpleCondition(value=1, operator="contains", operators_dict=operators_dict)

    condition.evaluate([1, 2, 3])
    assert (condition.match, condition.match_detail) == (True, [1,2,3])
    condition.evaluate([2, 3, 4])
    assert (condition.match, condition.match_detail) == (False, [2,3,4])

def test_contains_string(operators_dict):
    condition = SimpleCondition(value="Santiago", operator="contains", operators_dict=operators_dict)

    condition.evaluate("Santiago Alvarez")
    assert (condition.match, condition.match_detail) == (True, "Santiago Alvarez")
    condition.evaluate("Zapata Alvarez")
    assert (condition.match, condition.match_detail) == (False, "Zapata Alvarez")

def test_contains_bool_array(operators_dict):
    condition = SimpleCondition(value=True, operator="contains", operators_dict=operators_dict)

    condition.evaluate([True, True])
    assert (condition.match, condition.match_detail) == (True, [True, True])
    condition.evaluate([False, False])
    assert (condition.match, condition.match_detail) == (False, [False, False])
