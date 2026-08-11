from __future__ import annotations

import json

try:
    with open('example.txt') as file:
        json_string = file.read()
        print(json_string)
        data = json.loads(json_string)

    for key, value in data.items():
        print(f"{key}: {value}")

    data['adress'] = '123 Main St'

    json_string_updated = json.dumps(data)

    print(json_string_updated)
    data = json.loads(json_string_updated)
    data.pop('is_employee', None)  # Remove the "is_employee" key if it exists
    try:
        del data['is_employee']  # Remove the "is_employee" key if it exists
    except KeyError:
        print("Error: Key 'is_employee' not found in the dictionary.")
    # Output: {"name": "Alice", "age": 30, "adress": "123 Main St"}
    print(data)
except FileNotFoundError:
    print('Error: The file does not exist.')
except PermissionError:
    print('Error: You do not have permission to read this file.')
except Exception as e:
    print(f"An unexpected error occurred: {e}")
