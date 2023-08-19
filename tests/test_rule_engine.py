from python_rule_engine import RuleEngine


def test_basic_rule_on_dict():
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

