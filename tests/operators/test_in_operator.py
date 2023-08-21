from python_rule_engine.models.simple_condition import SimpleCondition


def test_in_int(operators_dict):
    condition = SimpleCondition(value=[1, 2, 3], operator="in", operators_dict=operators_dict)

    condition.evaluate(1)
    assert (condition.match, condition.match_detail) == (True, 1)
    condition.evaluate(4)
    assert (condition.match, condition.match_detail) == (False, 4)

def test_in_float(operators_dict):
    condition = SimpleCondition(value=[1.1, 2.2, 3.3], operator="in", operators_dict=operators_dict)

    condition.evaluate(1.1)
    assert (condition.match, condition.match_detail) == (True, 1.1)
    condition.evaluate(4.4)
    assert (condition.match, condition.match_detail) == (False, 4.4)

def test_in_str(operators_dict):
    condition = SimpleCondition(value=["Santiago", "Alvarez"], operator="in", operators_dict=operators_dict)

    condition.evaluate("Santiago")
    assert (condition.match, condition.match_detail) == (True, "Santiago")
    condition.evaluate("Zapata")
    assert (condition.match, condition.match_detail) == (False, "Zapata")

def test_in_bool(operators_dict):
    condition = SimpleCondition(value=[True, False], operator="in", operators_dict=operators_dict)

    condition.evaluate(True)
    assert (condition.match, condition.match_detail) == (True, True)
    condition.evaluate(None)
    assert (condition.match, condition.match_detail) == (False, None)
