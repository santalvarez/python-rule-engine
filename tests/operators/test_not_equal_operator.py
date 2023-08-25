from python_rule_engine.models.simple_condition import SimpleCondition


def test_not_equal_str(operators_dict):
    condition = SimpleCondition(value="Santiago", operator="not_equal", operators_dict=operators_dict)

    condition.evaluate("Santiago")
    assert (condition.match, condition.match_detail) == (False, "Santiago")
    condition.evaluate("Not Santiago")
    assert (condition.match, condition.match_detail) == (True, "Not Santiago")

def test_not_equal_int(operators_dict):
    condition = SimpleCondition(value=12345, operator="not_equal", operators_dict=operators_dict)

    condition.evaluate(12345)
    assert (condition.match, condition.match_detail) == (False, 12345)
    condition.evaluate(12346)
    assert (condition.match, condition.match_detail) == (True, 12346)

def test_not_equal_bool(operators_dict):
    condition = SimpleCondition(value=True, operator="not_equal", operators_dict=operators_dict)

    condition.evaluate(True)
    assert (condition.match, condition.match_detail) == (False, True)
    condition.evaluate(False)
    assert (condition.match, condition.match_detail) == (True, False)
