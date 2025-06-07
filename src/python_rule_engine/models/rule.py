from typing import Dict, Optional, Type

from pydantic import BaseModel, Field, model_validator
from pydantic.json_schema import SkipJsonSchema

from ..operators import Operator
from .multi_condition import MultiCondition


class Rule(BaseModel):
    name: str = Field(..., description="The name of the rule")
    description: Optional[str] = Field(None, description="A description of the rule")
    extra: Dict = Field({}, description="Extra metadata for the rule")
    event: Dict = {}
    conditions: MultiCondition = Field(..., description="The conditions that must be met for the rule to trigger")

    operators_dict: SkipJsonSchema[Dict[str, Type[Operator]]] = Field(
        ...,
        description="A dictionary of operators to use in the conditions",
        exclude=True)

    @model_validator(mode="before")
    @classmethod
    def set_operators_dict(cls, values):
        values.get("conditions", {})["operators_dict"] = values["operators_dict"]
        return values
