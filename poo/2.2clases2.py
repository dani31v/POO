import matplotlib.pyplot as plt
class Point2D:
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y
    def Change_X(self, x):
        self.x = x
    def Change_Y(self, y):
        self.y = y
    def Print_Values(self):
        print(f"({self.x}, {self.y})")
    def Add_to_X(self, x):
        self.x += x
    def Add_to_Y(self, y):
        self.y += y
    def Add_to_XY(self, x, y):
        self.x += x
        self.y += y
    def Add_Point(self, point):
        self.x += point.x
        self.y += point.y
    def Scale_values(self, scale_factor):
        self.x *= scale_factor
        self.y *= scale_factor

class Line2D:
    def __init__(self, p1, p2):
        self.point1 = p1
        self.point2 = p2
    def Calculate_midPoint(self):
        x = (self.point1.x + self.point2.x)/2
        y = (self.point1.y + self.point2.y)/2
        self.midPoint = Point2D(x, y)
    def Get_midPoint(self):
        self.Calculate_midPoint()
        return self.midPoint
    def Print_Values(self):
        self.Calculate_midPoint()
        print(f"P1: ({self.point1.x}, {self.point1.y})")
        print(f"P2: ({self.point2.x}, {self.point2.y})")
        print(f"MP: ({self.midPoint.x}, {self.midPoint.y})")
    def DrawLine(self):
        x = [self.point1.x, self.point2.x, self.midPoint.x]
        y = [self.point1.y, self.point2.y, self.midPoint.y]
        plt.plot(x,y)
        plt.show()

point1 = Point2D(1,1)
point2 = Point2D(2,2)

point1.Print_Values()
point2.Print_Values()

point2.Add_Point(point1)
point2.Scale_values(2)

line = Line2D(point1, point2)
line.Print_Values()
line.DrawLine()