import unittest
from rvvup.client import RvvupClient


class TestRvvupClient(unittest.TestCase):
    def setUp(self):
        self.client = RvvupClient(
            endpoint="https://example.com/graphql",
            merchant_id="test_merchant_id",
            auth_token="test_auth_token",
            user_agent="test_user_agent",
        )

    def test_ping(self):
        self.assertFalse(self.client.ping())  # Replace with a mock or a real test


if __name__ == "__main__":
    unittest.main()
