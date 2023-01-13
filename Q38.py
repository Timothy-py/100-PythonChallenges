from math import pi
# Define a class named Circle which can be constructed by a radius. The Circle class
# has a method which can compute the area.


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def calArea(self):
        area = round(pi * self.radius ** 2, 2)
        print("The area of a circle with radius, %s = %s" %
              (self.radius, area))


cir = Circle(5)
cir.calArea()
