from laboratorio2_1 import parse_json_string


def test_parse_json_string_returns_dict():
    json_text = '{"name": "Alice", "age": 30}'
    result = parse_json_string(json_text)

    assert result == {"name": "Alice", "age": 30}
