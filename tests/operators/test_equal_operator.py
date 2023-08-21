from python_rule_engine.models.simple_condition import SimpleCondition


def test_equal_string(operators_dict):
    condition = SimpleCondition(value="Santiago", operator="equal", operators_dict=operators_dict)

    condition.evaluate("Santiago")
    assert (condition.match, condition.match_detail) == (True, "Santiago")
    condition.evaluate("Not Santiago")
    assert (condition.match, condition.match_detail) == (False, "Not Santiago")

def test_equal_int(operators_dict):
    condition = SimpleCondition(value=12345, operator="equal", operators_dict=operators_dict)

    condition.evaluate(12345)
    assert (condition.match, condition.match_detail) == (True, 12345)
    condition.evaluate(12346)
    assert (condition.match, condition.match_detail) == (False, 12346)

def test_equal_bool(operators_dict):
    condition = SimpleCondition(value=True, operator="equal", operators_dict=operators_dict)

    condition.evaluate(True)
    assert (condition.match, condition.match_detail) == (True, True)
    condition.evaluate(False)
    assert (condition.match, condition.match_detail) == (False, False)