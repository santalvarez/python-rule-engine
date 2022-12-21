from python_rule_engine.models import SimpleCondition
from python_rule_engine.operators import (Operator, Equal, NotEqual, LessThan,
                        LessThanInclusive, GreaterThan, GreaterThanInclusive,
                        In, NotIn, Contains, NotContains)


def test_equal_operator():
    condition1 = SimpleCondition(value="Santiago", operator="equal")
    condition2 = SimpleCondition(value=12345, operator="equal")
    condition3 = SimpleCondition(value=True, operator="equal")
    
    assert Equal.match(condition1, "Santiago", None) == (True, "Santiago")
    assert Equal.match(condition1, "Not Santiago", None) == (False, "Not Santiago")

    assert Equal.match(condition2, 12345, None) == (True, 12345)
    assert Equal.match(condition2, 12346, None) == (False, 12346)

    assert Equal.match(condition3, True, None) == (True, True)
    assert Equal.match(condition3, False, None) == (False, False)

def test_not_equal_operator():
    condition1 = SimpleCondition(value="Santiago", operator="not_equal")
    condition2 = SimpleCondition(value=12345, operator="not_equal")
    condition3 = SimpleCondition(value=True, operator="not_equal")

    assert NotEqual.match(condition1, "Santiago", None) == (False, "Santiago")
    assert NotEqual.match(condition1, "Not Santiago", None) == (True, "Not Santiago")

    assert NotEqual.match(condition2, 12345, None) == (False, 12345)
    assert NotEqual.match(condition2, 12346, None) == (True, 12346)

    assert NotEqual.match(condition3, True, None) == (False, True)
    assert NotEqual.match(condition3, False, None) == (True, False)

def test_less_than_operator():
    condition1 = SimpleCondition(value=10, operator="less_than")
    condition2 = SimpleCondition(value=10.5, operator="less_than")
    condition3 = SimpleCondition(value="Santiago", operator="less_than")

    assert LessThan.match(condition1, 5, None) == (True, 5)
    assert LessThan.match(condition1, 15, None) == (False, 15)

    assert LessThan.match(condition2, 10.4, None) == (True, 10.4)
    assert LessThan.match(condition2, 10.6, None) == (False, 10.6)

    assert LessThan.match(condition3, "Alvarez", None) == (True, "Alvarez")
    assert LessThan.match(condition3, "Zapata", None) == (False, "Zapata")

def test_less_than_inclusive_operator():
    condition1 = SimpleCondition(value=10, operator="less_than_inclusive")
    condition2 = SimpleCondition(value=10.5, operator="less_than_inclusive")
    condition3 = SimpleCondition(value="Santiago", operator="less_than_inclusive")

    assert LessThanInclusive.match(condition1, 5, None) == (True, 5)
    assert LessThanInclusive.match(condition1, 15, None) == (False, 15)
    assert LessThanInclusive.match(condition1, 10, None) == (True, 10)

    assert LessThanInclusive.match(condition2, 10.4, None) == (True, 10.4)
    assert LessThanInclusive.match(condition2, 10.6, None) == (False, 10.6)
    assert LessThanInclusive.match(condition2, 10.5, None) == (True, 10.5)

    assert LessThanInclusive.match(condition3, "Alvarez", None) == (True, "Alvarez")
    assert LessThanInclusive.match(condition3, "Zapata", None) == (False, "Zapata")
    assert LessThanInclusive.match(condition3, "Santiago", None) == (True, "Santiago")

def test_greater_than_operator():
    condition1 = SimpleCondition(value=10, operator="greater_than")
    condition2 = SimpleCondition(value=10.5, operator="greater_than")
    condition3 = SimpleCondition(value="Santiago", operator="greater_than")

    assert GreaterThan.match(condition1, 5, None) == (False, 5)
    assert GreaterThan.match(condition1, 15, None) == (True, 15)

    assert GreaterThan.match(condition2, 10.4, None) == (False, 10.4)
    assert GreaterThan.match(condition2, 10.6, None) == (True, 10.6)

    assert GreaterThan.match(condition3, "Alvarez", None) == (False, "Alvarez")
    assert GreaterThan.match(condition3, "Zapata", None) == (True, "Zapata")

def test_greater_than_inclusive_operator():
    condition1 = SimpleCondition(value=10, operator="greater_than_inclusive")
    condition2 = SimpleCondition(value=10.5, operator="greater_than_inclusive")
    condition3 = SimpleCondition(value="Santiago", operator="greater_than_inclusive")

    assert GreaterThanInclusive.match(condition1, 5, None) == (False, 5)
    assert GreaterThanInclusive.match(condition1, 15, None) == (True, 15)
    assert GreaterThanInclusive.match(condition1, 10, None) == (True, 10)

    assert GreaterThanInclusive.match(condition2, 10.4, None) == (False, 10.4)
    assert GreaterThanInclusive.match(condition2, 10.6, None) == (True, 10.6)
    assert GreaterThanInclusive.match(condition2, 10.5, None) == (True, 10.5)

    assert GreaterThanInclusive.match(condition3, "Alvarez", None) == (False, "Alvarez")
    assert GreaterThanInclusive.match(condition3, "Zapata", None) == (True, "Zapata")
    assert GreaterThanInclusive.match(condition3, "Santiago", None) == (True, "Santiago")

def test_in_operator():
    condition1 = SimpleCondition(value=[1, 2, 3], operator="in")
    condition2 = SimpleCondition(value=["Santiago", "Alvarez"], operator="in")
    condition3 = SimpleCondition(value=[True, False], operator="in")

    assert In.match(condition1, 1, None) == (True, 1)
    assert In.match(condition1, 4, None) == (False, 4)

    assert In.match(condition2, "Santiago", None) == (True, "Santiago")
    assert In.match(condition2, "Zapata", None) == (False, "Zapata")

    assert In.match(condition3, True, None) == (True, True)
    assert In.match(condition3, None, None) == (False, None)

def test_not_in_operator():
    condition1 = SimpleCondition(value=[1, 2, 3], operator="not_in")
    condition2 = SimpleCondition(value=["Santiago", "Alvarez"], operator="not_in")
    condition3 = SimpleCondition(value=[True, False], operator="not_in")

    assert NotIn.match(condition1, 1, None) == (False, 1)
    assert NotIn.match(condition1, 4, None) == (True, 4)

    assert NotIn.match(condition2, "Santiago", None) == (False, "Santiago")
    assert NotIn.match(condition2, "Zapata", None) == (True, "Zapata")

    assert NotIn.match(condition3, True, None) == (False, True)
    assert NotIn.match(condition3, None, None) == (True, None)

def test_contains_operator():
    condition1 = SimpleCondition(value=1, operator="not_contains")
    condition2 = SimpleCondition(value="Santiago", operator="not_contains")
    condition3 = SimpleCondition(value=True, operator="not_contains")

    assert Contains.match(condition1, [1, 2, 3], None) == (True, [1,2,3])
    assert Contains.match(condition1, [2, 3, 4], None) == (False, [2,3,4])

    assert Contains.match(condition2, ["Santiago", "Alvarez"], None) == (True, ["Santiago", "Alvarez"])
    assert Contains.match(condition2, ["Zapata", "Alvarez"], None) == (False, ["Zapata", "Alvarez"])

    assert Contains.match(condition3, [True, True], None) == (True, [True, True])
    assert Contains.match(condition3, [False, False], None) == (False, [False, False])


def test_not_contains_operator():
    condition1 = SimpleCondition(value=1, operator="not_contains")
    condition2 = SimpleCondition(value="Santiago", operator="not_contains")
    condition3 = SimpleCondition(value=True, operator="not_contains")

    assert NotContains.match(condition1, [1, 2, 3], None) == (False, [1,2,3])
    assert NotContains.match(condition1, [2, 3, 4], None) == (True, [2,3,4])

    assert NotContains.match(condition2, ["Santiago", "Alvarez"], None) == (False, ["Santiago", "Alvarez"])
    assert NotContains.match(condition2, ["Zapata", "Alvarez"], None) == (True, ["Zapata", "Alvarez"])

    assert NotContains.match(condition3, [True, True], None) == (False, [True, True])
    assert NotContains.match(condition3, [False, False], None) == (True, [False, False])


def test_custom_operator():
    class EqualLowercase(Operator):
        id = "equal_lowercase"

        @staticmethod
        def match(condition, obj_value, run_condition):
            return condition.value.lower() == obj_value.lower(), obj_value

    assert EqualLowercase.match(SimpleCondition(value="Santiago", operator="equal_lowercase"), "SANTIAGO", None) == (True, "SANTIAGO")
