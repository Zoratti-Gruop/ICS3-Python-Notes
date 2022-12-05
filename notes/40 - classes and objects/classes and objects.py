class Point:
    """ Point class represents and manipulates x,y coords. 表示并操作x,y坐标。"""

    def __init__(self, xIn=0, yIn=0):
        """ Create a new point at x, y 在x，y创建一个新的点 """
        self.x = xIn
        self.y = yIn
        
    def __str__(self):
        return f"({self.x}, {self.y})"

    def distanceFromOrigin(self):
        """ Compute my distance from the origin计算我与原点的距离 """
        return ((self.x ** 2) + (self.y ** 2)) ** 0.5
# Other statements outside the class continue below here.
#END OF THE CLASS POINT

class Rectangle:
    """ A class to manufacture rectangle objects一个制造矩形对象的class """

    def __init__(self, posn, w, h):
        """ Initialize rectangle at posn, with width w, height h 在posn处初始化矩形，宽度为w，高度为h """
        self.corner = posn
        self.width = w
        self.height = h

    def __str__(self):
        return  "({0}, {1}, {2})".format(self.corner, self.width, self.height)
        

a = Point()
print(f'{a}')
b = Point(4,5)
print(f'{b}')

box = Rectangle(Point(0, 0), 100, 200)