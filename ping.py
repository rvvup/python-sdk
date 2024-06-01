from dotenv import load_dotenv

from rvvup import RvvupClient

load_dotenv()

client = RvvupClient()

response = client.ping()
print(f"Pong received at: {response}")
