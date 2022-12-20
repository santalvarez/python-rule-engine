from python_rule_engine import RuleEngine


def test_basic_rule():
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
                    "field": "$.person.name",
                    "value": "Santiago",
                    "operator": "equal"
                },
                {
                    "field": "$.person.last_name",
                    "value": "Alvarez",
                    "operator": "equal"
                }
            ]
        }
    }

    engine = RuleEngine([rule])

    results = engine.evaluate(obj)

    assert results[0].conditions.match is True
