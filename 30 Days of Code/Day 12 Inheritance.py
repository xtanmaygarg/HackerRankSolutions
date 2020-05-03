class Person:
	def __init__(self, firstName, lastName, idNumber):
		self.firstName = firstName
		self.lastName = lastName
		self.idNumber = idNumber
	def printPerson(self):
		print("Name:", self.lastName + ",", self.firstName)
		print("ID:", self.idNumber)

class Student(Person):
    def __init__(self, firstName, lastName, idNum, scores):
        super().__init__(firstName, lastName, idNum)
        self.scores = scores
    
    def calculate(self):
        Avg = sum(self.scores) / len(self.scores)
        if Avg < 40:
            return "T"
        elif Avg < 55:
            return "D"
        elif Avg < 70:
            return "P"
        elif Avg < 80:
            return "A"
        elif Avg < 90:
            return "E"
        else:
            return "O"

line = input().split()
firstName = line[0]
lastName = line[1]
idNum = line[2]
numScores = int(input()) # not needed for Python
scores = list( map(int, input().split()) )
s = Student(firstName, lastName, idNum, scores)
s.printPerson()
print("Grade:", s.calculate())
