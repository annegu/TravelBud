class Assignment:
    def __init__(self, id, name, dueDate):
        self.id = id
        self.name = name
        self.dueDate = dueDate
        self.classRating = 0
        self.numDone = 0

class Student: 
    def __init__(self):
        self.courses = []
 
class StudentCourseData:
  def __init__(self):
    self.labsCompleted = []
    self.PSCompleted = []

  def addLab(rating):
        labNum = len(labsCompleted)
        labsCompleted.append(labNum + 1, rating)
        
  def addPS(rating):
        PSnum = len(PScompleted)
        PScompleted.append(PSnum + 1, rating)

class Course:
  def __init__(self, cCode, numLab, numLec, numProb):
    self.courseCode = cCode
    self.numStudents = 1
    self.numLabs = numLab
    self.numLectures = numLec
    self.numPSets = numProb
    self.labs = []
    self.problemSets = []

  def addStudent():
    numStudents = numStudents + 1 #every time a new student adds the course to their page

  def createLabsList():
    i = 0
    while i < numLab:
      labs.append(Assignment(i, "Lab " + str(i), dueDate))  # how does dueDate get here though

  def createPSetsList():
    i = 0
    while i < numProb:
      problemSets.append(Assignment(i, "Problem Set " + str(i), dueDate))

  def printCourse(self):
    print(self.courseCode, self.numStudents, self.numLabs, self.numLectures, self.numPSets)

  
    
  