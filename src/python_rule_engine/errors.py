from pydantic import ValidationError

class RuleEngineBaseError(Exception):
    """ Base Rule Engine Exception """

class DuplicateOperatorError(RuleEngineBaseError):
    """ Raised when there is already a operator with the same ID
    loaded in the engine """

class JSONPathValueNotFoundError(RuleEngineBaseError):
    """ Raised when the value indicated by 'path' could not be found
    on the object."""

class RuleDecodeError(RuleEngineBaseError):
    """ Base error for all rule decoding errors """

class InvalidRuleSchemaError(RuleDecodeError):
    """ Raised when the field of the provided rule don't match with the rule's schema """

class InvalidRuleTypeError(RuleDecodeError):
    """ Raised when the provided rule is of an incorrect type """

class InvalidRuleJSONError(RuleDecodeError):
    """ Raised when the rule can't be converted to JSON.
    This will be raised when a provided string rule has invalid JSON format """

