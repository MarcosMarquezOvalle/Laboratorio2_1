import json
from typing import Any

try:
    with open("example.txt", "r") as file:
        json_string = file.read()
        print(json_string)
        data = json.loads(json_string)

    print(data["name"])         # Output: Alice
    print(data["age"])          # Output: 30
    print(data["is_employee"])  # Output: True
    data["adress"] = "123 Main St"
    json_string_updated = json.dumps(data)
    print(json_string_updated)  # Output: {"name": "Alice", "age": 30, "is_employee": true, "adress": "123 Main St"}
    data = json.loads(json_string_updated)
    data.pop("is_employee", None)  # Remove the "is_employee" key if it exists
    try:
        del data["is_employee"]  # Remove the "is_employee" key if it exists
    except KeyError:
        print("Error: Key 'is_employee' not found in the dictionary.")
    print(data)  # Output: {"name": "Alice", "age": 30, "adress": "123 Main St"}
except FileNotFoundError:
    print("Error: The file does not exist.")
except PermissionError:
    print("Error: You do not have permission to read this file.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
