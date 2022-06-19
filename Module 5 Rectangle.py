# Imports the Graphics library so that we are able to use the (Point class, __init__, __str___,...)
# With this library youre also able to open windows and code different graphic interations. 
from Graphics import*

# Point class stores mathematical points which was imported from the Graphics library
class Point:
    # Initialize the Point (self, x, y)
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Rectangle:
    # Initialize the Rectangle
    def __init__(self, posn, w, h):
        self.corner = posn
        self.width = w
        self.height = h

    def __str__(self):
        return "({0}, {1}, {2})".format(self.corner, self.width, self.height)

# To create_rectangle
# Creates a new instance of a Rectangle
def create_rectangle (x, y, width, height):
    posn = Point (x,y)
    rect = Rectangle (posn, width, height)
    return rect

# To str_rectangle 
# convert given Rectangle instance into string of form (x, y, width, height)
def str_rectangle (rect):
    return (rect.corner.x, rect.corner.y, rect.width, rect.height)

# To shift_rectangle
# change the x and y coordinates of the given Rectangle instance
def shift_rectangle (rect, dx, dy):
    rect.corner.x += dx
    rect.corner.y += dy

# To offset_rectangle
# create a new Rectangle instance which is offset from the given instance in x and y coordinates by dx and dy respectively
def offset_rectangle (rect, dx, dy):
    x = rect.corner.x + dx
    y = rect.corner.y + dy
    return (create_rectangle(x, y, rect.width, rect.height))

# Testing the given code with each group printing its own line.
r1 = create_rectangle (10, 20, 30, 40)
print (str_rectangle(r1))

shift_rectangle (r1, -10, -20)
print (str_rectangle(r1))

print (str_rectangle(r1))

r2 = offset_rectangle (r1, 100, 100)
print (str_rectangle(r1))
print (str_rectangle(r2))
