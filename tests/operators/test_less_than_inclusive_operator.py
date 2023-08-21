from python_rule_engine.models.simple_condition import SimpleCondition


def test_less_than_inclusive_int(operators_dict):
    condition = SimpleCondition(value=10, operator="less_than_inclusive", operators_dict=operators_dict)

    condition.evaluate(5)
    assert (condition.match, condition.match_detail) == (True, 5)
    condition.evaluate(15)
    assert (condition.match, condition.match_detail) == (False, 15)
    condition.evaluate(10)
    assert (condition.match, condition.match_detail) == (True, 10)

def test_less_than_inclusive_float(operators_dict):
    condition = SimpleCondition(value=10.5, operator="less_than_inclusive", operators_dict=operators_dict)

    condition.evaluate(10.4)
    assert (condition.match, condition.match_detail) == (True, 10.4)
    condition.evaluate(10.6)
    assert (condition.match, condition.match_detail) == (False, 10.6)
    condition.evaluate(10.5)
    assert (condition.match, condition.match_detail) == (True, 10.5)

def test_less_than_inclusive_str(operators_dict):
    condition = SimpleCondition(value="Santiago", operator="less_than_inclusive", operators_dict=operators_dict)

    condition.evaluate("Alvarez")
    assert (condition.match, condition.match_detail) == (True, "Alvarez")
    condition.evaluate("Zapata")
    assert (condition.match, condition.match_detail) == (False, "Zapata")
    condition.evaluate("Santiago")
    assert (condition.match, condition.match_detail) == (True, "Santiago")
