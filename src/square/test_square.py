# square/test_square.py

from square import Square

def test_square():
    # Create an instance of the Square class
    square = Square(4)
    
    # Test the initial side length
    assert square.get_side() == 4, "Initial side length should be 4"
    
    # Test the initial area
    assert square.calculate_area() == 16, "Initial area should be 16"
    
    # Change the side length
    square.set_side(7)
    
    # Test the updated side length
    assert square.get_side() == 7, "Updated side length should be 7"
    
    # Test the updated area
    assert square.calculate_area() == 49, "Updated area should be 49"
    
    # Display the area (this is more of a visual check)
    square.display_area()

if __name__ == "__main__":
    test_square()
    print("All tests passed.")
