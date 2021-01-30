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


#Student Class
class Student: 
  def __init__(self):
    self.courses = []

  def addCourse(self, cCode, data):
    self.courses.append((cCode, data))

        


class StudentCourseData:
  def __init__(self):
    self.labsCompleted = []
    self.PSCompleted = []
    self.lecsCompleted = []

  def addLab(self, rating):
    labNum = len(self.labsCompleted)
    self.labsCompleted.append((labNum, rating))
      
  def addPS(self, rating):
    PSnum = len(self.PSCompleted)
    self.PSCompleted.append((PSnum , rating))

  def addLec(self, rating):
    lecNum = len(self.lecsCompleted)
    self.lecsCompleted.append((lecNum , rating))



class Course:
  def __init__(self, cCode, numLab, numLec, numProb):
    self.courseCode = cCode
    self.numStudents = 1
    self.numLabs = numLab
    self.numLectures = numLec
    self.numPSets = numProb
    self.labs = []
    self.problemSets = []
    self.lectures = []

  def addStudent(self):
    self.numStudents += 1

  def createLabsList(self):
    i = 0
    while i < int(self.numLabs):
      self.labs.append(Assignment(i + 1, "Lab " + str(i + 1)))
      i += 1
  
  def createPSetsList(self):
    i = 0
    while i < int(self.numPSets):
      self.problemSets.append(Assignment(i + 1, "Assignment " + str(i + 1)))
      i += 1

  def createLecturesList(self):
    i = 0
    while i < int(self.numLectures):
      self.lectures.append(Assignment(i + 1, "Lecture " + str(i + 1)))
      i += 1
      
  # for debugging
  def printCourse(self):
    print(self.courseCode, self.numStudents, self.numLabs, self.numLectures, self.numPSets)

  
    
  