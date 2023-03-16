class RuleEngineBaseException(Exception):
    """ Base Rule Engine Exception """

class OperatorNotFoundError(RuleEngineBaseException):
    """ Raised when the specified operator is not found in the engine """

class DuplicateOperatorError(RuleEngineBaseException):
    """ Raised when there is already a operator with the same ID
    loaded in the engine """

class JSONPathValueNotFound(RuleEngineBaseException):
    """ Raised when the value indicated by 'path' could not be found
    on the object."""
