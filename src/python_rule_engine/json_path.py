from typing import Any

from jsonpath_ng import parse
from pydantic_core import core_schema

from .errors import JSONPathValueNotFoundError


class JSONPath(str):
    def __new__(cls, value):
        self = super().__new__(cls, value)
        self.parsed =  parse(self)
        return self

    @classmethod
    def __get_pydantic_core_schema__(cls, source_type, handler):
        return core_schema.no_info_after_validator_function(cls, handler(str))

    def get_value_from(self, obj: Any) -> Any:
        result = self.parsed.find(obj)
        if len(result) == 0:
            raise JSONPathValueNotFoundError(f"Value not found at path {self}")

        if len(result) == 1:
            return result[0].value

        return [r.value for r in result]
