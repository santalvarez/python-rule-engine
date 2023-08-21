
def validate_value(value, type_, name, nullable=False):
    if not nullable and value is None:
        raise ValueError(f"{name} cannot be None")
    if not isinstance(value, type_):
        raise ValueError(f"{name} must be of type {type_.__name__}")
    return value