from quadratic import QuadraticEquation

if __name__ == "__main__":
    # Coefficients
    a = 34
    b = 68
    c = -510

    # Create an instance of QuadraticEquation
    equation = QuadraticEquation(a, b, c)

    # Find and print the positive root
    positive_root = equation.get_positive_root()
    print("The positive root is:", positive_root)