import random

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
        return sum(self.scores) / len(self.scores)
    
    def getHighScore(self):
        """Returns the highest score."""
        return max(self.scores)

    def __eq__(self, other):
        """Tests if two students are equal based on their names."""
        return self.name == other.name

    def __lt__(self, other):
        """Tests if one student's name is less than the other's."""
        return self.name < other.name

    def __ge__(self, other):
        """Tests if one student's name is greater than or equal to the other's."""
        return self.name >= other.name
 
    def __str__(self):
        """Returns the string representation of the student."""
        return "Name: " + self.name  + "\nScores: " + \
               " ".join(map(str, self.scores))

def main():
    """A simple test."""
    # Create some Student objects
    student1 = Student("Elly", 5)
    student2 = Student("Ice", 5)
    student3 = Student("Neo", 5)
    student4 = Student("Elmo", 5)
    
    # Put the students into a list
    students = [student1, student2, student3, student4]
    
    # Shuffle the list
    random.shuffle(students)
    
    # Sort the list
    students.sort()
    
    # Display the students' information
    for student in students:
        print(str(student))

if __name__ == "__main__":
    main()