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

    def equal(self, other):
        "returns if equal or not"
        if (self.name == other.name):
            return "It is equal"
        else:
            return " It is not equal"

    def less(self, other):
        "returns if less than or not"
        if (self.name < other.name):
            return "It is less"
        else:
            return " It is not less"
    
    def greater(self, other):
        "returns if equal or not"
        if (self.name > other.name):
            return "It is greater than"
        elif self.name == other.name:
            return "Both are equal"
        else:
            "Not greater than or equal"

def main():
    """A simple test."""
    student = Student("Josh", 5)
    print(student)
    for i in range(1, 6):
        student.setScore(i, 100)
    print(student)

if __name__ == "__main__":
    main()

