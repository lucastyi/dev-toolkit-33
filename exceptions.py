class InputValidationError(Exception):
    pass

def validate_input(user_input):
    if not isinstance(user_input, dict):
        raise InputValidationError('Input must be a dictionary')
    if 'x' not in user_input or 'y' not in user_input:
        raise InputValidationError('Input must contain x and y keys')
    if not isinstance(user_input['x'], int) or not isinstance(user_input['y'], int):
        raise InputValidationError('x and y must be integers')
    if user_input['x'] < 0 or user_input['y'] < 0:
        raise InputValidationError('x and y must be non-negative')

# Example usage within a main processing loop
input_data = {'x': 100, 'y': 200}
try:
    validate_input(input_data)
    # Proceed with processing
except InputValidationError as e:
    print(f'Input error: {e}')