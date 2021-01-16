from flask import Flask, render_template
app = Flask(__name__)



@app.route("/")
def homepage():
    """View function for Home Page."""
    return render_template("home.html")


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


class Assignment:
    def __init__(self, id, name, dueDate, worth, classRating, numDone):
        self.id = id
        self.name = name
        self.dueDate = dueDate
        self.worth = worth
        self.classRating = 0
        self.numDone = 0

class Student: 
    def __init__(self, courses, courseData):
        self.courses = []
        self.courseData = []
        


if __name__ == "__main__":
    app.run()#debug=True





