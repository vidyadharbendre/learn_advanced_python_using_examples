from quadratic.quadratic_equation import QuadraticEquation

if __name__ == "__main__":
    a, b, c = 1, -3, 2
    equation = QuadraticEquation(a, b, c)
    print(f"Equation: {a}x^2 + {b}x + {c} = 0")
    print(f"Discriminant: {equation.calculate_discriminant()}")
    roots = equation.find_roots()
    print(f"Roots: {roots}")
    print(f"Positive Root: {equation.get_positive_root()}")
