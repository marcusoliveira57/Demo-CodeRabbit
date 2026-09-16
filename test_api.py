import os
import unittest
from unittest.mock import Mock, patch

from api import fetch


class FetchTests(unittest.TestCase):
    def test_fetch_requires_api_key(self):
        environment = os.environ.copy()
        environment.pop("API_KEY", None)

        with patch.dict(os.environ, environment, clear=True):
            with self.assertRaisesRegex(KeyError, "API_KEY"):
                fetch("users")

    def test_fetch_sends_key_as_parameter_and_checks_response(self):
        response = Mock()
        response.json.return_value = {"id": 1}

        with patch.dict(os.environ, {"API_KEY": "test-key"}):
            with patch("api.requests.get", return_value=response) as get:
                result = fetch("/users")

        get.assert_called_once_with(
            "https://api.exemplo.com/users",
            params={"key": "test-key"},
            timeout=10,
        )
        response.raise_for_status.assert_called_once_with()
        self.assertEqual(result, {"id": 1})


if __name__ == "__main__":
    unittest.main()
