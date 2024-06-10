def helper_function():
    return "This is a helper function."


def validate_inputs(params, expected_types):
    """
    Validates the input parameters for the financial calculations.

    :param params: Dictionary of parameter names and values.
    :param expected_types: Dictionary of parameter names and their expected types.
    :raises ValueError: If any of the inputs are invalid.
    """
    for key, value in params.items():
        if key in expected_types and not isinstance(value, expected_types[key]):
            expected_type = expected_types[key]
            if isinstance(expected_type, tuple):
                expected_type_str = 'one of ' + ', '.join([t.__name__ for t in expected_type])
            else:
                expected_type_str = expected_type.__name__
            raise ValueError(f"{key} must be {expected_type_str}")