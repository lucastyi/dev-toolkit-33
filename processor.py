import json
import logging

class ProcessorError(Exception):
    pass

def process_data(input_data):
    if not isinstance(input_data, list):
        raise ProcessorError('Input must be a list')
    if len(input_data) == 0:
        raise ProcessorError('Input list cannot be empty')
    try:
        results = []
        for item in input_data:
            if not isinstance(item, dict):
                raise ProcessorError(f'Expected dict but got {type(item).__name__}')
            result = json.dumps(item)
            results.append(result)
    except json.JSONDecodeError as e:
        logging.error('JSON decoding error: %s', e)
        raise ProcessorError('Error processing JSON data')
    except Exception as e:
        logging.error('Unexpected error: %s', e)
        raise ProcessorError('An unexpected error occurred')
    return results

if __name__ == '__main__':
    test_data = [{'name': 'Alice'}, {'name': 'Bob'}]
    try:
        output = process_data(test_data)
        print(output)
    except ProcessorError as e:
        logging.error('Processing failed: %s', e)