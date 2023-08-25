from python_rule_engine.models.simple_condition import SimpleCondition


def test_greater_than_inclusive_int(operators_dict):
    condition = SimpleCondition(value=10, operator="greater_than_inclusive", operators_dict=operators_dict)

    condition.evaluate(5)
    assert (condition.match, condition.match_detail) == (False, 5)
    condition.evaluate(15)
    assert (condition.match, condition.match_detail) == (True, 15)
    condition.evaluate(10)
    assert (condition.match, condition.match_detail) == (True, 10)

def test_greater_than_inclusive_float(operators_dict):
    condition = SimpleCondition(value=10.5, operator="greater_than_inclusive", operators_dict=operators_dict)

    condition.evaluate(10.4)
    assert (condition.match, condition.match_detail) == (False, 10.4)
    condition.evaluate(10.6)
    assert (condition.match, condition.match_detail) == (True, 10.6)
    condition.evaluate(10.5)
    assert (condition.match, condition.match_detail) == (True, 10.5)

def test_greater_than_inclusive_str(operators_dict):
    condition = SimpleCondition(value="Santiago", operator="greater_than_inclusive", operators_dict=operators_dict)

    condition.evaluate("Alvarez")
    assert (condition.match, condition.match_detail) == (False, "Alvarez")
    condition.evaluate("Zapata")
    assert (condition.match, condition.match_detail) == (True, "Zapata")
    condition.evaluate("Santiago")
    assert (condition.match, condition.match_detail) == (True, "Santiago")
