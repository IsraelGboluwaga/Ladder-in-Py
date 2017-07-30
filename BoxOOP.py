'''
As an exercise, write a function named moveRect that takes a
Rectangle and two parameters named dx and dy. It should change
the location of the rectangle by adding dx to the x coordinate of corner
and adding dy to the y coordinate of corner.
'''

'''
The conversion to classes and methods have not worked yet
'''


class Rectangle:
    def __init__(self, x= 0, y= 0):
        self.x = x
        self.y = y
    def __str__(self):
        return str(self.x), str(self.y)

class Point:
    pass

box = Rectangle(9,5)
# box.x = 0.0
# box.y = 0.0

def moveRect(box, dx, dy):
    import copy
    newbox = copy.deepcopy(box)
    newbox.x = box.x + dx
    newbox.y = box.y + dy
    return newbox

def printPoint(p):
    return p.x, p.y

# newbox = moveRect(box, 20.0, 30.0)

# print printPoint(newbox)
print box
