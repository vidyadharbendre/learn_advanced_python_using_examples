# tests/test_extended_circle.py

import unittest
from circle.extended_circle import ExtendedCircle
import math

class TestExtendedCircle(unittest.TestCase):
    def setUp(self):
        """Set up test fixtures."""
        self.extended_circle = ExtendedCircle(5)

    def test_perimeter(self):
        """Test the perimeter calculation."""
        expected_perimeter = 2 * math.pi * 5  # Using math.pi for consistency
        self.assertAlmostEqual(self.extended_circle.perimeter(), expected_perimeter, places=7)

if __name__ == "__main__":
    unittest.main()
