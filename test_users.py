import unittest
from unittest.mock import MagicMock, patch

from users import get_user


class GetUserTests(unittest.TestCase):
    def test_get_user_uses_parameterized_query(self):
        connection = MagicMock()
        db = connection.__enter__.return_value
        db.execute.return_value.fetchall.return_value = [(1, "User")]

        with patch("users.connect_db", return_value=connection):
            result = get_user("1 OR 1=1")

        db.execute.assert_called_once_with(
            "SELECT * FROM users WHERE id = ?",
            ("1 OR 1=1",),
        )
        connection.__exit__.assert_called_once()
        self.assertEqual(result, [(1, "User")])


if __name__ == "__main__":
    unittest.main()
