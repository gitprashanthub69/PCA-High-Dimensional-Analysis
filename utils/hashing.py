import hashlib
import json


def generate_sha256(data: dict) -> str:
    """
    Generates SHA-256 hash for transaction data
    """
    # Convert dictionary to consistent string
    data_string = json.dumps(data, sort_keys=True)

    sha = hashlib.sha256()
    sha.update(data_string.encode("utf-8"))

    return sha.hexdigest()
