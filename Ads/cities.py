import json
from pathlib import Path

def read_json_file(file_path: str) -> list[dict]:
    path = Path(file_path)
    if not path.exists():
        raise FileNotFoundError(f"File not found: {file_path}")

    with path.open("r", encoding="utf-8") as f:
        try:
            return json.load(f)
        except json.JSONDecodeError as e:
            raise ValueError(f"Invalid JSON format: {e}")


try:
    provinces = read_json_file("test.json")
    for province in provinces:
        print(f"{province['name']} ({province['tel_prefix']})")
except Exception as e:
    print(f"Error: {e}")