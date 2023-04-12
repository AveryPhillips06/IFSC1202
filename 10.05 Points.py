import math

class Point:
   def __init__(self, Xvalue, Yvalue):
       self.x = Xvalue
       self.y = Yvalue

   def ToString(self):
       return str(self.x) + "," + str(self.y)

def Distance(PointA, PointB):
   
   distance = math.sqrt((PointB.x - PointA.x)**2 + (PointB.y - PointA.y)**2)
   return distance


def MidPoint(PointA, PointB):
   
   midpoint_x = (PointA.x + PointB.x) / 2
   midpoint_y = (PointA.y + PointB.y) / 2
   midpoint = Point(midpoint_x, midpoint_y)
   return midpoint

def XAngle(PointA, PointB):
   
   slope = (PointB.y - PointA.y) / (PointB.x - PointA.x)
   angle = math.atan(slope) * 180 / math.pi
   return angle

with open("10.05 Points.txt", "r") as file:
   lines = file.readlines()
   for line in lines:
       data = line.strip().split(',')
       xa, ya, xb, yb = map(float, data)
       pointA = Point(xa, ya)
       pointB = Point(xb, yb)
       distance = Distance(pointA, pointB)
       midpoint = MidPoint(pointA, pointB)
       xangle = XAngle(pointA, pointB)
       print("Point A:", pointA.ToString())
       print("Point B:", pointB.ToString())
       print("Distance:", distance)
       print("Midpoint:", midpoint.ToString())
       print("XAngle:", xangle, "degrees")
       print("------------")

 