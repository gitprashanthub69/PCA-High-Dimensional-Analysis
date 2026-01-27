import hashlib
import json

def generate_sha256(data: dict) -> str:
    data_string = json.dumps(data, sort_keys=True)
    return hashlib.sha256(data_string.encode()).hexdigest()
