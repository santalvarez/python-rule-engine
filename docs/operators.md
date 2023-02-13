# Operators

## Default Operators

### Equal

- **id**: "equal"

- **description**: Compares if the value of the object is equal to the value of the condition.


### Not Equal

- **id**: "not_equal"
- **description**: Compares if the value of the object is not equal to the value of the condition.


### Greater Than

- **id**: "greater_than"

- **description**: Compares if the value of the object is greater than the value of the condition.


### Greater Than Inclusive

- **id**: "greater_than_inclusive"

- **description**: Compares if the value of the object is greater than or equal to the value of the condition.


### Less Than

- **id**: "less_than"

- **description**: Compares if the value of the object is less than the value of the condition.


### Less Than Inclusive

- **id**: "less_than_inclusive"

- **description**: Compares if the value of the object is less than or equal to the value of the condition.


### In

- **id**: "in"

- **description**: Compares if the value of the object is in the value of the condition.


### Not In

- **id**: "not_in"

- **description**: Compares if the value of the object is not in the value of the condition.


### Contains

- **id**: "contains"

- **description**: Compares if the value of the object contains the value of the condition.


### Not Contains

- **id**: "not_contains"

- **description**: Compares if the value of the object does not contain the value of the condition.


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
