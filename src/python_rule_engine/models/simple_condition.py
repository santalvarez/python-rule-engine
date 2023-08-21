from __future__ import annotations

from typing import Any, Optional

from ..exceptions import JSONPathValueNotFound
from ..json_path import JSONPath
from .condition import Condition
from ..operators import Operator


class SimpleCondition(Condition):
    def __init__(self, **data):
        super().__init__()
        self.operator: Operator = self.__validate_operator(data)
        self.path: Optional[JSONPath] = self.__validate_path(data)
        self.value: Any = data["value"]
        self.params = data.get('params', {})
        self.match_detail = None

    def __validate_path(self, data: dict) -> Optional[JSONPath]:
        if 'path' in data:
            return JSONPath(data['path'])
        return None

    def __validate_operator(self, data: dict) -> Operator:
        operators_dict = data['operators_dict']

        if 'operator' not in data:
            raise ValueError("Operator attribute missing")

        if data['operator'] not in operators_dict:
            raise ValueError("Specified operator not found in engine")

        # Initialize the found Operator type and pass self to init
        return operators_dict[data['operator']](self)

    def __obj_to_dict(self, obj: Any) -> Any:
        """ Recursively convert an object to a dict if possible

        :param Any obj: The object
        :return Any: The object as a dict or the original object
        """
        if isinstance(obj, dict):
            return {k: self.__obj_to_dict(v) for k, v in obj.items()}
        if hasattr(obj, "__dict__"):
            return self.__obj_to_dict(obj.__dict__)
        if isinstance(obj, (list, tuple)):
            return [self.__obj_to_dict(v) for v in obj]
        return obj


    def evaluate(self, obj: dict):
        """ Run the condition on an object

        :param Condition condition: The simple condition
        :param Any obj: The object
        :raises OperatorNotFoundError: If a referenced operator is not loaded
        :return condition: The condition with added result info
        """
        try:
            if self.path:
                path_obj = self.path.get_value_from(obj)
            else:
                path_obj = obj

            match, match_detail = self.operator.match(path_obj)
            self.match = match
            self.match_detail = self.__obj_to_dict(match_detail)
        except JSONPathValueNotFound as e:
            self.match = False
            self.match_detail = str(e)
