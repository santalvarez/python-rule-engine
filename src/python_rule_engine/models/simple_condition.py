from __future__ import annotations

from typing import Any, Dict, Optional

from pydantic import Field, model_validator, PrivateAttr
from pydantic.json_schema import SkipJsonSchema

from ..exceptions import JSONPathValueNotFound
from ..json_path import JSONPath
from ..operators import Operator, DEFAULT_OPERATORS
from .condition import Condition


class SimpleCondition(Condition):
    operators_dict: SkipJsonSchema[Dict] = Field(..., exclude=True, repr=False)
    _operator_object: SkipJsonSchema[Optional[Operator]] = PrivateAttr(None)

    path: Optional[JSONPath] = Field(None, description="A JSONPath expression to extract a value from the object")
    operator: str = Field(..., description="The operator to use for the comparison",
                          examples=[o.id for o in DEFAULT_OPERATORS])
    value: Any = Field(..., description="The value to compare against")
    params: dict = Field({}, description="Additional parameters for the operator")
    match_detail: SkipJsonSchema[Any] = None

    def __deepcopy__(self, memo=None):
        return self.model_copy(deep=False)

    @model_validator(mode="after")
    def validate_operator_object(self):
        if self.operator not in self.operators_dict:
            raise ValueError("Specified operator not found in engine")

        self._operator_object = self.operators_dict[self.operator](self)

        return self

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

            match, match_detail = self._operator_object.match(path_obj)
            self.match = match
            self.match_detail = self.__obj_to_dict(match_detail)
        except JSONPathValueNotFound as e:
            self.match = False
            self.match_detail = str(e)
