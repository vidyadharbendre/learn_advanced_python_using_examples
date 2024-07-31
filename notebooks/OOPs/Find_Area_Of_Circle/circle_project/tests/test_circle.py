# tests/test_circle.py

import unittest
from circle.circle import Circle

class TestCircle(unittest.TestCase):
    def setUp(self):
        """Set up test fixtures."""
        self.circle = Circle(5)

    def test_area(self):
        """Test the area calculation."""
        expected_area = 3.14159 * 5 * 5
        self.assertAlmostEqual(self.circle.area(), expected_area, places=5)

if __name__ == "__main__":
    unittest.main()
