# Define a class named Rectangle which can be constructed by a length and width.
# The Rectangle class has a method which can compute the area.

class Rectangle:
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def calArea(self):
        area = self.length * self.breadth
        print("The area of a rectangle with length, %s and breadth, %s = %s" %
              (self.length, self.breadth, area))


rec = Rectangle(4, 8)
rec.calArea()
