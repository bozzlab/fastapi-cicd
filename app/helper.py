import uuid

def generate_id() -> str:
    return str(uuid.uuid4().hex)[0:9]