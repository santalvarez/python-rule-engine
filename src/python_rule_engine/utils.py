
def validate_value(value, type_, name, nullable=False):
    if nullable and value is None:
        return value
    if not isinstance(value, type_):
        raise ValueError(f"{name} must be of type {type_.__name__}")
    return value
