# Operators

## Custom Operator

To create your own operator you need to implement the `Operator` class.

```python
from python_rule_engine import Operator, RuleEngine

class EqualLowercase(Operator):
    id = "equal_lowercase"

    @staticmethod
    def match(condition, obj_value, run_condition):
        return condition.value.lower() == obj_value.lower(), obj_value


# Load operator to engine
engine = RuleEngine([...], operators=[EqualLowercase])
```
