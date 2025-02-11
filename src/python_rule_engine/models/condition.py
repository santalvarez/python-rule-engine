from pydantic import BaseModel
from pydantic.json_schema import SkipJsonSchema


class Condition(BaseModel):
    match: SkipJsonSchema[bool] = False

    def evaluate(self, obj):
        raise NotImplementedError
