# main.py
from circle.circle import Circle
from circle.extended_circle import ExtendedCircle

# if __name__ == "__main__":
#     radius = 5
#     circle = Circle(radius)
#     print(f"Area of circle with radius {radius}: {circle.area()}")

#     extended_circle = ExtendedCircle(radius)
#     print(f"Perimeter of circle with radius {radius}: {extended_circle.perimeter()}")

def main():
    radius = 5
    circle = Circle(radius)
    print(f"The area of the circle with radius {radius} is {circle.area()}")
    extented_circle = ExtendedCircle(radius)
    print(f"The Perimeter of the circle with radius {radius} is {extented_circle.perimeter()}")

if __name__ == "__main__":
    main()
