from python_rule_engine.models.simple_condition import SimpleCondition


def test_deepcopy_operator_not_copied(operators_dict):
    sc = SimpleCondition(path="$.foo", operator="equal",
                         value="bar", operators_dict=operators_dict)
    sc_copy = sc.model_copy(deep=True)
    sc.match = True

    # assert that operator kept the same reference
    assert id(sc.operator) == id(sc_copy.operator)
    assert id(sc._operator_object) == id(sc_copy._operator_object)
    assert sc_copy.match == False


