from typing import Any

from jsonpath_ng import parse

from .exceptions import JSONPathValueNotFound


class JSONPath:
    def __init__(self, path: str) -> None:
        self.original_path: str = path
        self.jsonpath_parsed = parse(path)

    def get_value_from(self, obj: Any) -> Any:
        result = self.jsonpath_parsed.find(obj)
        if len(result) == 0:
            raise JSONPathValueNotFound(f"Value not found at path {self.original_path}")

        if len(result) == 1:
            return result[0].value

        return [r.value for r in result]
