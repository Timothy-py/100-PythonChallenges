# Define a class named Shape and its subclass Square.
# The Square class has an init function which takes a length as argument.
# Both classes have a area function which can print the area of the shape where Shape's area is 0 by default.


class Shape:
    def __init__(self):
        pass

    def area(self):
        area = 0
        print(f"Shape's area = {area}")


class Square(Shape):
    def __init__(self, length):
        super().__init__()
        self.length = length

    def area(self):
        area = self.length ** 2
        print(f"Area of square with side {self.length} = {area}")


sq = Square(6)
sq.area()
