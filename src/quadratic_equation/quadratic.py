import math

class QuadraticEquation:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    
    def calculate_discriminant(self):
        return self.b ** 2 - 4 * self.a * self.c
    
    def find_roots(self):
        discriminant = self.calculate_discriminant()
        
        if discriminant >= 0:
            root1 = (-self.b + math.sqrt(discriminant)) / (2 * self.a)
            root2 = (-self.b - math.sqrt(discriminant)) / (2 * self.a)
            return root1, root2
        else:
            return None, None
    
    def get_positive_root(self):
        root1, root2 = self.find_roots()
        if root1 is not None and root2 is not None:
            if root1 > 0 and root2 > 0:
                return min(root1, root2)
            elif root1 > 0:
                return root1
            elif root2 > 0:
                return root2
            else:
                return "No positive root"
        else:
            return "No real roots"
