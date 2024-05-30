import os

from rvvup import RvvupClient

token = os.environ["RVVUP_API_KEY"]

if token is None or len(token) == 0:
    raise ValueError("RVVUP_API_KEY environment variable must be set")

client = RvvupClient(auth_token=token, user_agent="ping/1.0")

response = client.ping()
print(f"Pong received at: {response}")
