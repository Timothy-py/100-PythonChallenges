# A robot moves in a plane starting from the original point (0,0). The robot can move toward UP, DOWN, LEFT and RIGHT
# with a given steps. The trace of robot movement is shown as the following: UP 5 DOWN 3 LEFT 3 RIGHT 2
# The numbers after the direction are steps. Write a program to compute the distance from current position after a
# sequence of movement and original point. If the distance is a float, then just print the nearest integer.
# Example:
# If the following tuples are given as input to the program:
# UP 5
# DOWN 3
# LEFT 3
# RIGHT 2
# Then, the output of the program should be: 2


up = float(input('UP = '))
down = float(input('DOWN = '))
left = float(input('LEFT = '))
right = float(input('RIGHT = '))

up, down, left, right = int(up), int(down), int(left), int(right)

y_axis = up - down
x_axis = right - left

distance = int(sqrt(y_axis**2 + x_axis**2))

print('Total Distance = %s' % distance)
