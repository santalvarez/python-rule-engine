from python_rule_engine import RuleEngine, Operator


def test_basic_rule_on_dict():
    obj = {
        "person": {
            "name": "Santiago",
            "last_name": "Alvarez"
        }
    }

    rule = {
        "name": "basic_rule",
        "conditions": {
            "all": [
                {
                    "path": "$.person.name",
                    "value": "Santiago",
                    "operator": "equal"
                },
                {
                    "path": "$.person.last_name",
                    "value": "Alvarez",
                    "operator": "equal"
                }
            ]
        }
    }

    engine = RuleEngine([rule])

    results = engine.evaluate(obj)

    assert results[0].conditions.match is True


def test_basic_rule_on_object():
    class Person:
        def __init__(self):
            self.name = "Santiago"
            self.last_name = "Alvarez"

    class Example:
        def __init__(self):
            self.person = Person()

    obj = Example()

    rule = {
        "name": "basic_rule",
        "conditions": {
            "all": [
                {
                    "path": "$.person.name",
                    "value": "Santiago",
                    "operator": "equal"
                },
                {
                    "path": "$.person.last_name",
                    "value": "Alvarez",
                    "operator": "equal"
                }
            ]
        }
    }

    engine = RuleEngine([rule])

    results = engine.evaluate(obj)

    assert results[0].conditions.match is True

def test_custom_operator():
    class EqualLowercase(Operator):
        id = "equal_lowercase"

        @staticmethod
        def match(condition, obj_value, run_condition):
            return condition.value.lower() == obj_value.lower(), obj_value

    rule = {
        "name": "test-lowercase",
        "conditions": {
            "any": [
                {
                    "path": "$.person.name",
                    "value": "Santiago",
                    "operator": "equal_lowercase"
                }
            ]
        }
    }

    obj = {
        "person": {
            "name": "SANTIAGO",
        }
    }

    engine = RuleEngine([rule], [EqualLowercase])

    result = engine.evaluate(obj)

    assert result[0].conditions.match is True
