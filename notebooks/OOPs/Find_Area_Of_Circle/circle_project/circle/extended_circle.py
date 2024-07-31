from .circle import Circle
import math

class ExtendedCircle(Circle):
    def perimeter(self):
        return 2 * math.pi * self.radius
