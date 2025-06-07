# Rules

A basic rule consists of a name and a multi condition
```json
{
    "name": "test-rule",
    "conditions": {
        "all": [
            {""" condition1 """},
            {""" condition2 """}
        ]
    }
}
```

| key | description | type | required |
| --- | --- | --- | --- |
| name | The name of the rule | str | yes |
| description | A description of the rule. | str | no |
| conditions | A [multi condition](#multi-condition). All rules start with a multi condition. | dict | yes |
| extra | A dict that can be used to store extra information about the rule. | dict | no |

## Condition Types

### Simple Condition

A simple condition consists of an operator and a value.

```json
{
    "path" : "$.person.name",
    "operator": "equal",
    "value": "John"
}
```
Table describing the keys:

| key | description | type | required |
| --- | --- | --- | --- |
| operator | The operator to use to compare the object with the defined value. Find info on built-in operators and how to define your own [here](operators.md). | str | yes |
| path | A [JSONPath](https://goessner.net/articles/JsonPath/) expression indicating what attribute of the object to evaluate. Appart from accessing attributes it also supports accessing array elements by [index]. | str | no |
| value | The value that will be used to compare with the object. | any | yes |
| params | A dict that can provide the operator more information about how to process the object. | dict | no |


### Multi Condition

Contains either the **any**, **all** or **not** fields. These fields contain a list of conditions that can be simple, multi or a mix of both.

```json
{
    "all": [
        {
            "operator": "equal",
            "path": "$.person.name",
            "value": "John"
        },
        {
            "any": [
                {""" condition """}
            ]
        }
    ]
}
```

Only one of these fields can be present in a multi condition.
| key | description | type |
| --- | --- | --- |
| all | All conditions inside have to match. | list |
| any | One of the conditions inside have to match. | list |
| not | The result of the condition inside will be negated. | dict |


## Results

A rule result has the same structure as a rule but with two added fields.

**match(bool):** Indicates wether the condition matched.

**match_detail(any):** Contains details about the object that matched.
