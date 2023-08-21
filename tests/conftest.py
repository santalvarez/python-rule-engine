from pytest import fixture

from python_rule_engine.operators import (Contains, Equal, GreaterThan,
                                          GreaterThanInclusive, In, LessThan,
                                          LessThanInclusive, NotContains,
                                          NotEqual, NotIn)


@fixture
def operators_dict():
    return {
        "in": In,
        "not_in": NotIn,
        "equal": Equal,
        "not_equal": NotEqual,
        "less_than": LessThan,
        "less_than_inclusive": LessThanInclusive,
        "greater_than": GreaterThan,
        "greater_than_inclusive": GreaterThanInclusive,
        "contains": Contains,
        "not_contains": NotContains,
    }
