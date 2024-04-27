"""
File: student.py
Resources to manage a student's name and test scores.
"""

class Student(object):
    """Represents a student."""

    def __init__(self, name, number):
        """All scores are initially 0."""
        self.name = name
        self.scores = []
        for count in range(number):
            self.scores.append(0)

    def getName(self):
        """Returns the student's name."""
        return self.name
  
    def setScore(self, i, score):
        """Resets the ith score, counting from 1."""
        self.scores[i - 1] = score

    def getScore(self, i):
        """Returns the ith score, counting from 1."""
        return self.scores[i - 1]
   
    def getAverage(self):
        """Returns the average score."""
        return sum(self.scores) / len(self._scores)
    
    def getHighScore(self):
        """Returns the highest score."""
        return max(self.scores)
 
    def __str__(self):
        """Returns the string representation of the student."""
        return "Name: " + self.name  + "\nScores: " + \
               " ".join(map(str, self.scores))

    def __equal__(self, other):
        """Returns if the students are equal or not"""
        if (self.name == other.name):
            return "Equal"
        else:
            return "Not Equal"

    def __lessThan__(self, other):
        """Returns if the first instance is less than the second instance"""
        if (self.name < other.name):
            return "Less Than"
        else:
            return "Not Less Than"
    
    def __greaterThan__(self, other):
        """Returns if the first instance is greater than or equal to the second instance"""
        if (self.name > other.name):
            return "Greater Than"
        elif (self.name == other.name):
            return "Equal"
        else:
            return "Not Greater Than Nor Equal"

def main():
    """A simple test."""
    studentA = Student("Jarick", 5)
    print(studentA)
    for i in range(1, 6):
        studentA.setScore(i, 100)
    print(studentA)

    studentB = Student("Jam", 5)
    print(studentB)
    for i in range(1, 6):
        studentB.setScore(i, 100)
    print(studentB)

    print("\n--Results--")
    print(Student.__equal__(studentA, studentB))
    print(Student.__lessThan__(studentA, studentB))
    print(Student.__greaterThan__(studentA, studentB))
    print("\n")

if __name__ == "__main__":
    main()

