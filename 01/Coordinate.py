class Coordinate:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f'<{self.x}, {self.y}>'
    
    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y

        return Coordinate(x, y)
    
    def __sub__(self, other):
        x = self.x - other.x
        y = self.y - other.y

        return Coordinate(x, y)
        

c1 = Coordinate(7, 9)
c2 = Coordinate(4, 5)
c3 = c1 - c2

print(c1)
print(c2)
print(c3)
