class Time:
    def __init__(self, hours = 0, minutes = 0, seconds = 0):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def __str__(self):
        form = "%.2d : %.2d : %.2d" %(self.hours, self.minutes, self.seconds)
        return form

currentTime = Time(seconds= 35)
print currentTime

class Point:
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y
    def __str__(self):
        return "(" + str(self.x) + ", " + str(self.y) + ")"
    def __add__(self, other):
        return (self.x + other.x, self.y + other.y)
    def __sub__(self, other):
        return (self.x - other.x, self.y - self.y)
    def __mul__(self, other):
        return (self.x * other.x, self.y * other.y)
    def __rmul__(self, other):
        return (other * self.x, other * self.y)


# p = Point(2,4)
# q = Point(8,3)
# r = p + q
# s = q - p
# print p, q, r, s
# t = p * q
# print t, 2 * p