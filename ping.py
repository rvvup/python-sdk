import os

import jwt

from rvvup import RvvupClient

token = os.environ["RVVUP_API_KEY"]

if token is None or len(token) == 0:
    raise ValueError("RVVUP_API_KEY environment variable must be set")

payload = jwt.decode(token, options={"verify_signature": False})
audience = payload.get("aud")
merchant_id = payload.get("merchantId")

client = RvvupClient(
    endpoint=audience, merchant_id=merchant_id, auth_token=token, user_agent="ping/1.0"
)

response = client.ping()
print(f"Pong received at: {response}")
