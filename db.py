class Assignment:
    def __init__(self, id, name, dueDate, worth):
        self.id = id
        self.name = name
        self.dueDate = dueDate
        self.classRating = 0
        self.numDone = 0

class Student: 
    def __init__(self):
        self.courses = []
        self.courseData = []
        
class StudentCourseData:
  def __init__(self):
    self.labsCompleted = []
    self.PSCompleted = []

class Course:
  def __init__(self, cCode, numLab, numLec, numProb):
    self.courseCode = cCode
    self.numStudents = 1
    self.numLabs = numLab
    self.numLectures = numLec
    self.numPSets = numProb
    self.labs = []
    self.problemSets = []
