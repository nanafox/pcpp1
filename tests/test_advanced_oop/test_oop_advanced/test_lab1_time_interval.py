from unittest import TestCase

from advanced_oop.oop_advanced.labs.lab1_time_interval import TimeInterval


class TestTimeInterval(TestCase):
    """Test the TimeInterval class."""

    def test_add(self):
        """Test the addition of two TimeInterval objects."""
        interval1 = TimeInterval(hours=1, minutes=30, seconds=10)
        interval2 = TimeInterval(hours=0, minutes=45, seconds=20)
        result = interval1 + interval2
        self.assertEqual(str(result), "02:15:30")

    def test_subtract(self):
        """Test the subtraction of two TimeInterval objects."""
        interval1 = TimeInterval(hours=2, minutes=0, seconds=0)
        interval2 = TimeInterval(hours=0, minutes=30, seconds=30)
        result = interval1 - interval2
        self.assertEqual(str(result), "01:29:30")

    def test_multiply(self):
        """Test the multiplication of a TimeInterval object by a factor."""
        interval = TimeInterval(hours=1, minutes=0, seconds=0)
        factor = 3
        result = interval * factor
        self.assertEqual(str(result), "03:00:00")

    def test_invalid_type(self):
        """Test if TypeError is raised for invalid argument types."""
        with self.assertRaises(TypeError):
            interval = TimeInterval(hours=1, minutes=0, seconds=0)
            interval + "invalid"

    def test_string_representation(self):
        """Test the string representation of a TimeInterval object."""
        interval = TimeInterval(hours=10, minutes=5, seconds=30)
        self.assertEqual(str(interval), "10:05:30")
