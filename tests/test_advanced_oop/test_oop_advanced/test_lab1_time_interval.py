from unittest import TestCase

from advanced_oop.oop_advanced.labs.lab_time_interval import TimeInterval


class TestTimeInterval(TestCase):
    """Test the TimeInterval class."""

    def test_add(self):
        """Test the addition of two TimeInterval objects."""
        time_1 = TimeInterval(hours=1, minutes=30, seconds=10)
        time_2 = TimeInterval(hours=0, minutes=45, seconds=20)
        interval = time_1 + time_2
        self.assertEqual(str(interval), "02:15:30")

    def test_subtract(self):
        """Test the subtraction of two TimeInterval objects."""
        time_1 = TimeInterval(hours=2, minutes=0, seconds=0)
        time_2 = TimeInterval(hours=0, minutes=30, seconds=30)
        interval = time_1 - time_2
        self.assertEqual(str(interval), "01:29:30")

    def test_multiply(self):
        """Test the multiplication of a TimeInterval object by an interval."""
        time = TimeInterval(hours=1, minutes=0, seconds=0)
        factor = 3
        interval = time * factor
        self.assertEqual(str(interval), "03:00:00")

    def test_invalid_type(self):
        """Test if TypeError is raised for invalid argument types."""
        with self.assertRaises(TypeError):
            time = TimeInterval(hours=1, minutes=0, seconds=0)
            time + "invalid"

    def test_string_representation(self):
        """Test the string representation of a TimeInterval object."""
        time = TimeInterval(hours=10, minutes=5, seconds=30)
        self.assertEqual(str(time), "10:05:30")

    def test_add_with_integer(self):
        """Test the add of a TimeInterval object with number of seconds"""
        time = TimeInterval(hours=1, minutes=4, seconds=5)
        interval = time + 60
        self.assertEqual(str(interval), "01:05:05")

    def test_sub_with_integer(self):
        """Test sub add of a TimeInterval object with number of seconds"""
        time = TimeInterval(hours=1, minutes=4, seconds=5)
        interval = time - 60
        self.assertEqual(str(interval), "01:03:05")

    def test_invalid_seconds(self):
        """Test an operation with an invalid type."""
        with self.assertRaises(TypeError):
            TimeInterval(hours=1, minutes=4, seconds=5) + 50.4

    def test_unknown_operation(self):
        """Test an invalid operation"""
        with self.assertRaises(TypeError):
            TimeInterval(hours=1, minutes=0, seconds=0) / 3600.54
