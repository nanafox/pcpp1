from unittest import TestCase

from advanced_oop.oop_foundations.labs.lab1_model_phone import MobilePhone


class TestMobilePhone(TestCase):
    def setUp(self):
        self.mobile = MobilePhone("012-456-2211")

    def test_turn_on(self):
        """Test the `turn_on` method."""
        self.assertEqual(
            self.mobile.turn_on(),
            f"mobile phone {self.mobile.number} is turned on",
        )

    def test_turn_off(self):
        """Test the `turn_off` method."""
        self.assertEqual(self.mobile.turn_off(), "mobile phone is turned off")

    def test_call(self):
        """Test the `call` method."""
        self.assertEqual(self.mobile.call(), f"calling {self.mobile.number}")
