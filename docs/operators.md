# Operators

## Default Operators

| Operator             | ID                      | Description                                                                                                     |
|----------------------|-------------------------|-----------------------------------------------------------------------------------------------------------------|
| Equal                | "equal"                 | Compares if the value of the object is equal to the value of the condition.                                    |
| Not Equal            | "not_equal"             | Compares if the value of the object is not equal to the value of the condition.                                |
| Greater Than         | "greater_than"          | Compares if the value of the object is greater than the value of the condition.                                |
| Greater Than Inclusive| "greater_than_inclusive" | Compares if the value of the object is greater than or equal to the value of the condition.                  |
| Less Than            | "less_than"             | Compares if the value of the object is less than the value of the condition.                                   |
| Less Than Inclusive  | "less_than_inclusive"   | Compares if the value of the object is less than or equal to the value of the condition.                       |
| In                   | "in"                    | Compares if the value of the object is in the value of the condition.                                          |
| Not In               | "not_in"                | Compares if the value of the object is not in the value of the condition.                                      |
| Contains             | "contains"              | Compares if the value of the object contains the value of the condition.                                       |
| Not Contains         | "not_contains"          | Compares if the value of the object does not contain the value of the condition.                               |

## Custom Operator

To create your own operator you need to implement the `Operator` class.

```python
from python_rule_engine import Operator, RuleEngine

class EqualLowercase(Operator):
    id = "equal_lowercase"

    def match(self, obj_value):
        return self.condition.value.lower() == obj_value.lower(), obj_value


# Load operator to engine
engine = RuleEngine([...], operators=[EqualLowercase])
```
