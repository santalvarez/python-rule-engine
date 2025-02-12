from python_rule_engine.decoder import RuleDecoder
from python_rule_engine.errors import RuleDecodeError


def test_rule_decode_success():
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

def test_rule_decode_error():
    d = RuleDecoder()

    r = "foobar"

    try:
        d.decode_str_rule(r)
        assert False
    except RuleDecodeError:
        assert True
    except Exception as e:
        assert False
