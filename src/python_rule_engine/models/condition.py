from pydantic import BaseModel


class Condition(BaseModel):
    match: bool = False

    def evaluate(self, obj):
        raise NotImplementedError
