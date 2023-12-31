from python_rule_engine import RuleEngine


def test_rule_with_all_condition():
    obj = {
        "person": {
            "name": "Santiago",
            "last_name": "Alvarez"
        }
    }

    rule = {
        "name": "basic_rule",
        "description": "Basic rule to test the engine",
        "extra": {
            "some_field": "some_value"
        },
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

def test_rule_with_any_condition():
    obj = {
        "person": {
            "name": "Santiago",
            "last_name": "Alvarez"
        }
    }

    rule = {
        "name": "basic_rule",
        "conditions": {
            "any": [
                {
                    "path": "$.person.name",
                    "value": "Martin",
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

def test_rule_with_not_condition():
    obj = {
        "person": {
            "name": "Santiago",
            "last_name": "Alvarez"
        }
    }

    rule = {
        "name": "basic_rule",
        "conditions": {
            "not": {  # None of the conditions inside "all" should be true
                "all": [
                    {
                        "path": "$.person.name",
                        "value": "Martin",
                        "operator": "equal"
                    },
                    {
                        "path": "$.person.last_name",
                        "value": "Palermo",
                        "operator": "equal"
                    }
                ]
            }
        }
    }

    engine = RuleEngine([rule])

    results = engine.evaluate(obj)

    assert results[0].conditions.match is True
