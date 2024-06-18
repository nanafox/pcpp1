from io import StringIO
from unittest import TestCase
from unittest.mock import patch

from advanced_oop.oop_foundations.labs.lab2_apple_shop_tracking import (
    ApplePackage,
)


class TestApplePackage(TestCase):
    """Tests the ApplePackage class."""

    def tearDown(self):
        """Zero out the processed apples after each test run."""
        ApplePackage.apples_processed = 0

    def test_check_limit_with_one_extra_apple(self):
        """Test the `check_limit` method with an extra apple."""
        with self.assertRaises(SystemExit):
            with patch("sys.stdout", new=StringIO()):
                for _ in range(1001):
                    ApplePackage()

        self.assertNotEqual(ApplePackage.apples_processed, 1001)

    def test_check_limit_five_apples(self):
        """Test the behavior when only five apples are created."""
        with patch("sys.stdout", new=StringIO()):
            for _ in range(5):
                ApplePackage()

        self.assertEqual(ApplePackage.apples_processed, 5)

    def test_check_limit_with_one_apple(self):
        """Test the behavior when a single apple is created."""
        with patch("sys.stdout", new=StringIO()):
            ApplePackage()

        self.assertEqual(ApplePackage.apples_processed, 1)

    def test_check_limit_with_500_apples(self):
        """Test the behavior with 500 apples."""
        with patch("sys.stdout", new=StringIO()):
            for _ in range(500):
                ApplePackage()
