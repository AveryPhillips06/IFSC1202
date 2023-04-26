import math

class Triangle:
    def __init__(self, s1, s2, s3):
        self.s1 = s1
        self.s2 = s2
        self.s3 = s3

    def type(self):
        if self.s1 == self.s2 == self.s3:
            return "Equilateral"
        elif self.s1 == self.s2 or self.s2 == self.s3 or self.s1 == self.s3:
            return "Isosceles"
        else:
            return "Scalene"

    def perimeter(self):
        return self.s1 + self.s2 + self.s3

    def area(self):
        s = (self.s1 + self.s2 + self.s3) / 2
        return math.sqrt(s * (s - self.s1) * (s - self.s2) * (s - self.s3))

    def angles(self):
        a = math.degrees(math.acos((self.s2**2 + self.s3**2 - self.s1**2) / (2 * self.s2 * self.s3)))
        b = math.degrees(math.acos((self.s1**2 + self.s3**2 - self.s2**2) / (2 * self.s1 * self.s3)))
        c = math.degrees(math.acos((self.s1**2 + self.s2**2 - self.s3**2) / (2 * self.s1 * self.s2)))
        return [a, b, c]

TriangleList = []

with open("Exam Three Triangles.txt", "r") as f:
    for line in f:
        s1, s2, s3 = map(float, line.strip().split(", "))
        t = Triangle(s1, s2, s3)
        TriangleList.append(t)
print("Type\t\tSide 1\tSide 2\tSide 3\t\tPerimeter\tArea\tAngle 1\t\tAngle 2\t\tAngle 3")
for t in TriangleList:
    ttype = t.type()
    s1 = "{:.3f}".format(t.s1)
    s2 = "{:.3f}".format(t.s2)
    s3 = "{:.3f}".format(t.s3)
    p = "{:.3f}".format(t.perimeter())
    a = "{:.3f}".format(t.area())
    angles = [ "{:.3f}".format(angle) for angle in t.angles() ]
    print(f"{ttype}\t{s1}\t{s2}\t{s3}\t\t{p}\t\t{a}\t{angles[0]}\t\t{angles[1]}\t\t{angles[2]}")