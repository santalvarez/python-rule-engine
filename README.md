# python-rule-engine

[![pypi](https://img.shields.io/pypi/v/python-rule-engine.svg)](https://pypi.python.org/pypi/python-rule-engine)
[![versions](https://img.shields.io/pypi/pyversions/python-rule-engine.svg)](https://github.com/santalvarez/python-rule-engine)
[![license](https://img.shields.io/github/license/pydantic/pydantic.svg)](https://github.com/pydantic/pydantic/blob/main/LICENSE)


A rule engine where rules are defined in JSON format. The syntax of the rules belongs to the [json-rules-engine](https://github.com/CacheControl/json-rules-engine) javascript library though it contains some changes to make it more powerfull.

- [Rule Syntax](docs/rules.md)
- [Operators](docs/operators.md)

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
                # JSONPath support
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

obj = {
    "person": {
        "name": "Lionel",
        "last_name": "Messi"
    }
}

engine = RuleEngine([rule])

results = engine.evaluate(obj)

```

## Generating rules with ChatGPT
You can leverage the Rule's model definition to generate rules using ChatGPT. The following example shows how to generate a rule using OpenAI's API. More info on how to use the API can be found [here](https://platform.openai.com/docs/guides/structured-outputs).

```python
from openai import OpenAI
from python_rule_engine import Rule


obj = {
    "player": {
        "name": "Lionel",
        "age": 34,
    }
}

client = OpenAI(api_key="your_api_key")

completion = client.beta.chat.completions.parse(
    model="gpt-4o-2024-08-06",
    messages=[
        {"role": "system", "content": "Generate a json rule that matches the following conditions:"},
        {"role": "user", "content": "Create a rule that matches if the player's name is Lionel and the player's age bigger than 30"},
    ],
    response_format=Rule,
)

rule = completion.choices[0].message.parsed

engine = RuleEngine([rule])

assert engine.evaluate(obj).match
```