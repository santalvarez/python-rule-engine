from python_rule_engine.decoder import RuleDecoder
from python_rule_engine.errors import (DuplicateOperatorError,
                                       InvalidRuleSchemaError,
                                       InvalidRuleTypeError)
from python_rule_engine.operators import Equal


def test_duplicate_operator_error():
    try:
        RuleDecoder(custom_operators=[Equal])
        assert False
    except DuplicateOperatorError:
        assert True
    except Exception:
        assert False

def test_decode_rule_success():
    d = RuleDecoder()

    r = {
        "name": "test",
        "conditions": {
            "all": [
                {
                    "path": "$.foo.bar",
                    "operator": "equal",
                    "value": "test"
                }
            ]
        }
    }

    try:
        d.decode_rule(r)
    except:
        assert False

def test_decode_rule_type_error():
    d = RuleDecoder()

    r = 123

    try:
        d.decode_rule(r)
        assert False
    except InvalidRuleTypeError:
        assert True
    except Exception:
        assert False

def test_decode_rule_schema_error():
    d = RuleDecoder()

    r = {
        "name": "test",
        "conditions": "foobar"
    }

    try:
        d.decode_rule(r)
        assert False
    except InvalidRuleSchemaError:
        assert True
    except Exception:
        assert False

def test_str_rule_decode_schema_error():
    d = RuleDecoder()

    r = "foobar"

    try:
        d.decode_str_rule(r)
        assert False
    except InvalidRuleSchemaError:
        assert True
    except Exception:
        assert False

def test_str_rule_decode_type_error():
    d = RuleDecoder()

    r = 123

    try:
        d.decode_str_rule(r)
        assert False
    except InvalidRuleTypeError:
        assert True
    except Exception:
        assert False

def test_decode_str_rules_success():
    d = RuleDecoder()

    r = [
        "{\"name\": \"test\", \"conditions\": {\"all\": [{\"path\": \"$.foo.bar\", \"operator\": \"equal\", \"value\": \"test\"}]}}",
        "{\"name\": \"test\", \"conditions\": {\"all\": [{\"path\": \"$.foo.bar\", \"operator\": \"equal\", \"value\": \"test\"}]}}"
    ]

    try:
        d.decode_str_rules(r)
    except Exception:
        assert False
