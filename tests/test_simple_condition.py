from python_rule_engine.models.simple_condition import SimpleCondition
import pytest
from python_rule_engine.operators import DEFAULT_OPERATORS


def test_deepcopy_operator_not_copied(operators_dict):
    sc = SimpleCondition(path="$.foo", operator="equal",
                         value="bar", operators_dict=operators_dict)
    sc_copy = sc.model_copy(deep=True)
    sc.match = True

    # assert that operator kept the same reference
    assert id(sc.operator) == id(sc_copy.operator)
    assert id(sc._operator_object) == id(sc_copy._operator_object)
    assert sc_copy.match == False


def test_invalid_operator():
    with pytest.raises(ValueError):
        SimpleCondition(path="$.foo", operator="invalid",
                         value="bar", operators_dict={})

def test_evaluate_json_path_not_found():
    operators_dict = {op.id: op for op in DEFAULT_OPERATORS}
    sc = SimpleCondition(path="$.foo", operator="equal",
                         value="bar", operators_dict=operators_dict)
    sc.evaluate({})
    assert sc.match == False
    assert sc.match_detail == "Value not found at path $.foo"

