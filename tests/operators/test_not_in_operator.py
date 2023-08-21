from python_rule_engine.models.simple_condition import SimpleCondition


def test_not_in_int(operators_dict):
    condition = SimpleCondition(value=[1, 2, 3], operator="not_in", operators_dict=operators_dict)

    condition.evaluate(1)
    assert (condition.match, condition.match_detail) == (False, 1)
    condition.evaluate(4)
    assert (condition.match, condition.match_detail) == (True, 4)

def test_not_in_str(operators_dict):
    condition = SimpleCondition(value=["Santiago", "Alvarez"], operator="not_in", operators_dict=operators_dict)

    condition.evaluate("Santiago")
    assert (condition.match, condition.match_detail) == (False, "Santiago")
    condition.evaluate("Zapata")
    assert (condition.match, condition.match_detail) == (True, "Zapata")

def test_not_in_bool(operators_dict):
    condition = SimpleCondition(value=[True, False], operator="not_in", operators_dict=operators_dict)

    condition.evaluate(True)
    assert (condition.match, condition.match_detail) == (False, True)
    condition.evaluate(None)
    assert (condition.match, condition.match_detail) == (True, None)
