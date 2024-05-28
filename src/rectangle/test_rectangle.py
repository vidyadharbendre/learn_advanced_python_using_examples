# rectangle/test_rectangle.py

from rectangle import Rectangle

def test_rectangle():
    # create an instance of rectangle class
    rectangle = Rectangle(3, 4)

    # Test the initial length
    assert rectangle.get_length() == 3, "Initial length should be 3"

    # Test the initial width
    assert rectangle.get_width() == 4, "Initial width should be 4"

    # Test the initial area
    assert rectangle.calculate_area() == 12, "Initial area should be 12"

    # Change the side length
    rectangle.set_length(5)

    # Test the updated side length
    assert rectangle.get_length() == 5, "Updated side length should be 5"

    # Change the side width
    rectangle.set_width(6)

    # Test the updated side width
    assert rectangle.get_width() == 6, "Updated side width should be 6"

    # Test the updated area
    assert rectangle.calculate_area() == 30, "Updated area should be 30"
    
    # Display the area (this is more of a visual check)
    rectangle.display_area()

if __name__ == "__main__":
    test_rectangle()
    print("All tests passed.")