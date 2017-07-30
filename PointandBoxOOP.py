class Point:
    pass

blank = Point()
blank.x = 2.
blank.y = 3.

nblank = Point()
nblank.x = 4.
nblank.y = 5.

def printPoint(p):
    return p.x, p.y
def printDimensions(p):
    return p.width, p.height, printPoint(p.corner)

class Rectangle:
    pass
box = Rectangle()
box.width = 200.0
box.height = 100.0
box.corner = Point()
box.corner.x = 0.0
box.corner.y = 0.0

def findCenter(box):
    p = Point()
    p.x = box.corner.x + box.width/2
    p.y = box.corner.y - box.height/2
    return p

def growRect(box, dwidth, dheight):
    box.width = box.width + dwidth
    box.height = box.height + dheight

bob = Rectangle()
bob.width = 400.0
bob.height = 200.0
bob.corner = Point()
bob.corner.x = 100.0
bob.corner.y = 250.0

growRect(box, 100.0, 50.0)
print printDimensions(bob)