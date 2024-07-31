#python -m unittest discover -s tests

import unittest
from quadratic.quadratic_equation import QuadraticEquation

class TestQuadraticEquation(unittest.TestCase):
    def test_discriminant(self):
        equation = QuadraticEquation(1, -3, 2)
        self.assertEqual(equation.calculate_discriminant(), 1)
    
    def test_roots(self):
        equation = QuadraticEquation(1, -3, 2)
        roots = equation.find_roots()
        self.assertAlmostEqual(roots[0], 2)
        self.assertAlmostEqual(roots[1], 1)
    
    def test_positive_root(self):
        equation = QuadraticEquation(1, -3, 2)
        self.assertAlmostEqual(equation.get_positive_root(), 1)
    
    def test_no_real_roots(self):
        equation = QuadraticEquation(1, 0, 1)
        roots = equation.find_roots()
        self.assertEqual(roots, (None, None))

    def test_no_positive_root(self):
        equation = QuadraticEquation(1, 2, 1)
        self.assertEqual(equation.get_positive_root(), "No positive root")

if __name__ == "__main__":
    unittest.main()
