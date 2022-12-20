# python-rule-engine

A rule engine where rules are defined in JSON format. The syntax of the rules belongs to the [json-rules-engine](https://github.com/CacheControl/json-rules-engine) javascript library though it contains some changes to make it more powerfull.

## Installation
```
pip install python-rule-engine
```

## Quick Example

```python
from python_rule_engine import RuleEngine

rule = {
    "name": "basic_rule",
    "conditions": {
        "all": [
            {
                "path": "$.person.name",
                "operator": "equal",
                "value": "Lionel"
            },
            {
                "path": "$.person.last_name",
                "operator": "equal",
                "value": "Messi"
            }
        ]
    }
}

# You can also pass a non-dict object to match its attributes
obj = {
    "person": {
        "name": "Lionel",
        "last_name": "Messi"
    }
}

engine = RuleEngine([rule])

results = engine.evaluate(obj)

```


