class RuleEngineBaseException(Exception):
    """ Base Rule Engine Exception """

class OperatorNotFoundError(RuleEngineBaseException):
    """ Raised when the specified operator is not found in the engine """

class DuplicateOperatorError(RuleEngineBaseException):
    """ Raised when there is already a operator with the same ID
    loaded in the engine """

class InvalidFieldTypeError(RuleEngineBaseException):
    """ Raised when field type is not `model` or `value` """

class ArrayRuleKeyError(RuleEngineBaseException):
    """ Raised when the `and` or `or` keys are not defined
    in the array rule """
