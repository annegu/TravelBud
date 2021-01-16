class Assignment:
  def __init__(self, id, name):
    self.id = id
    self.name = name
    # self.dueDate = dueDate
    self.classRating = 0
    self.numDone = 0

  # for debugging
  def printAssignment(self):
    print(self.id, self.name)

  def updateClassRating(self, numStudents, addedRating):
    self.classRating = (numStudents*classRating + addedRating) / (numStudents + 1)

  def updateNumDone(self):
    self.numDone += 1

    




class Student: 
  def __init__(self):
    self.courses = []

  def addCourse(self, cCode):
    self.courses.append((cCode, StudentCourseData()))





class StudentCourseData:
  def __init__(self):
    self.labsCompleted = []
    self.PSCompleted = []

  def addLab(self, rating):
    labNum = len(labsCompleted)
    self.labsCompleted.append((labNum + 1, rating))
    
    i = 0
    while i < len(labsCompleted):
      print(self.labsCompleted[i])

  
        
  def addPS(self, rating):
    PSnum = len(PScompleted)
    self.PScompleted.append((PSnum + 1, rating))




class Course:
  def __init__(self, cCode, numLab, numLec, numProb):
    self.courseCode = cCode
    self.numStudents = 1
    self.numLabs = numLab
    self.numLectures = numLec
    self.numPSets = numProb
    self.labs = []
    self.problemSets = []

  def addStudent(self):
    self.numStudents += 1

  def createLabsList(self):
    i = 0
    while i < int(self.numLabs):
      self.labs.append(Assignment(i + 1, "Lab " + str(i + 1)))  # should we ask for duedate for each assignment still or nah
      i += 1
  
  def createPSetsList(self):
    i = 0
    while i < int(self.numProb):
      self.problemSets.append(Assignment(i + 1, "Problem Set " + str(i + 1)))
      i += 1
      
  # for debugging
  def printCourse(self):
    print(self.courseCode, self.numStudents, self.numLabs, self.numLectures, self.numPSets)

  
    
  