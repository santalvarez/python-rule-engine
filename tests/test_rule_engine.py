from python_rule_engine import RuleEngine


def test_two_objects_with_same_rule_one_match():
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

    obj["person"]["name"] = "Martin"

    results = engine.evaluate(obj)

    assert len(results) == 0

def test_two_objects_with_same_rule_match_different_match_detail():
    obj = {
        "person": {
            "name": "Santiago",
        }
    }

    rule = {
        "name": "basic_rule",
        "description": "Basic rule to test the engine",
        "extra": {
            "some_field": "some_value"
        },
        "conditions": {
            "any": [
                {
                    "path": "$.person.name",
                    "value": "Santiago",
                    "operator": "equal"
                },
                {
                    "path": "$.person.name",
                    "value": "Martin",
                    "operator": "equal"
                }
            ]
        }
    }

    engine = RuleEngine([rule])

    results = engine.evaluate(obj)

    assert results[0].conditions.match is True
    assert results[0].conditions.any[0].match is True
    assert results[0].conditions.any[0].match_detail == "Santiago"

    obj["person"]["name"] = "Martin"

    results = engine.evaluate(obj)

    assert results[0].conditions.match is True
    assert results[0].conditions.any[0].match is False
    assert results[0].conditions.any[0].match_detail == "Martin"
    assert results[0].conditions.any[1].match_detail == "Martin"

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

def test_rule_engine_add_rule():
    obj = {
        "person": {
            "name": "Santiago",
            "last_name": "Alvarez"
        }
    }
    engine = RuleEngine([])

    engine.add_rule({"name": "test", "conditions": {"all": [{"path": "$.person.name", "value": "Santiago", "operator": "equal"}]}})

    results = engine.evaluate(obj)

    assert results[0].conditions.match is True

def test_rule_engine_add_str_rule():
    obj = {
        "person": {
            "name": "Santiago",
            "last_name": "Alvarez"
        }
    }

    engine = RuleEngine([])

    engine.add_str_rule('{"name": "test", "conditions": {"all": [{"path": "$.person.name", "value": "Santiago", "operator": "equal"}]}}')

    results = engine.evaluate(obj)

    assert results[0].conditions.match is True

def test_rule_engine_remove_rule():
    obj = {
        "person": {
            "name": "Santiago",
            "last_name": "Alvarez"
        }
    }
    engine = RuleEngine([])

    engine.add_rule({"name": "test", "conditions": {"all": [{"path": "$.person.name", "value": "Santiago", "operator": "equal"}]}})

    results = engine.evaluate(obj)

    assert results[0].conditions.match is True

    engine.remove_rule("test")

    assert not engine.evaluate(obj)
