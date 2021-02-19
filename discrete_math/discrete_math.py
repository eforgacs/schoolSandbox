class Shape(object):
    def __init__(self):
        self.sides = 0
        self.color = None


class Square(Shape):
    def __init__(self):
        super().__init__()
        self.sides = 4


class Triangle(Shape):
    def __init__(self):
        super().__init__()
        self.sides = 3


e, g, h, j = Square(), Square(), Square(), Square()
d, f, i = Triangle(), Triangle(), Triangle()

squares = {e, g, h, j}
triangles = {d, f, i}

e.color = "black"
g.color = "gray"
h.color = "gray"
j.color = "blue"

d.color = "black"
f.color = "gray"
i.color = "gray"

square_colors_with_different_triangle_colors = []

for square in squares:
    for triangle in triangles:
        if square.color != triangle.color:
            print("Square color " + square.color + " is different from Triangle color " + triangle.color)
            if square.color not in square_colors_with_different_triangle_colors:
                square_colors_with_different_triangle_colors.append(square.color)

print(square_colors_with_different_triangle_colors)
