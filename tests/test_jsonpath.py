from python_rule_engine import RuleEngine


def test_basic_jsonpath():
    obj = {
        "persons": [
            {
                "name": "Lionel",
                "last_name": "Messi"
            },
            {
                "name": "Cristiano",
                "last_name": "Ronaldo"
            },
            {
                "name": "Neymar",
                "last_name": "Jr"
            }
        ]
    }

    rule = {
        "name": "basic_rule",
        "description": "Basic rule to test the engine",
        "conditions": {
            "all": [
                {
                    "path": "$.persons[*].name",
                    "value": "Cristiano",
                    "operator": "contains"
                }
            ]
        }
    }

    engine = RuleEngine([rule])

    results = engine.evaluate(obj)

    assert results[0].conditions.match is True
