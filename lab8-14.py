class Square:
    def __init__(self, s): self.s = s
    def perimeter(self): return 4 * self.s

class Circle:
    def __init__(self, r): self.r = r
    def perimeter(self): return 2 * 3.1416 * self.r

class Triangle:
    def __init__(self, x, y, z): self.x, self.y, self.z = x, y, z
    def perimeter(self): return self.x + self.y + self.z


for shape in [Square(6), Circle(5), Triangle(2,3,4)]:
    print(shape.perimeter())
