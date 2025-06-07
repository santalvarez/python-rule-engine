from pytest import fixture

from python_rule_engine.operators import DEFAULT_OPERATORS

@fixture
def operators_dict():
    # convert the list of operators to a dictionary
    return {op.id: op for op in DEFAULT_OPERATORS}

