class Student:
   def __init__(self, firstname, lastname, tnumber, scores):
       self.FirstName = firstname
       self.LastName = lastname
       self.TNumber = tnumber
       self.Grades = [score for score in scores if score] # Filter out blank scores


   def RunningAverage(self):
       if not self.Grades:
           return 0.0
       return sum(float(grade) for grade in self.Grades) / len(self.Grades)

   def TotalAverage(self):
       if not self.Grades:
           return 0.0
       return sum(float(grade) if grade else 0.0 for grade in self.Grades) / len(self.Grades)

   def LetterGrade(self):
       average = self.TotalAverage()
       if average >= 90:
           return "A"
       elif average >= 80:
           return "B"
       elif average >= 70:
           return "C"
       elif average >= 60:
           return "D"
       else:
           return "F"

with open('10.04 StudentScores.txt') as f:
   for line in f:
       parts = line.strip().split(',')
       firstname = parts[0]
       lastname = parts[1]
       tnumber = parts[2]
       scores = parts[3:]
       student = Student(firstname, lastname, tnumber, scores)
       print(f"{student.FirstName} {student.LastName} ({student.TNumber}) has a {student.LetterGrade()} with a total average of {student.TotalAverage()} and a running average of {student.RunningAverage()}")
 
    