from flask import Flask, render_template
app = Flask(__name__)

COURSES = []


@app.route("/")
def homepage():
    """View function for Home Page."""
    return render_template("coursePage.html", courseName = "Ece216")

@app.route("/signup", methods=["POST", "GET"])
def signup():
    form = SignUpForm()
    return render_template("signup.html", form = form)

class StudentCourseData:
  def __init__(self):
    self.labsCompleted = []
    self.PSCompleted = []

<<<<<<< HEAD
class Course:
  def __init__(self, cCode, numLab, numLec, numProb):
    self.courseCode = cCode
    self.numStudents = 1
    self.numLabs = numLab
    self.numLectures = numLec
    self.numPSets = numProb
    self.labs = []
    self.problemSets = []

=======
if __name__ == "__main__":
    app.run()#debug=True
>>>>>>> 3c1d531e974dd21d4ec30c9c22263c78fac5a861

class Assignment:
    def __init__(self, id, name, dueDate, worth):
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
        
<<<<<<< HEAD


if __name__ == "__main__":
    app.run()#debug=True





=======
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
>>>>>>> 3c1d531e974dd21d4ec30c9c22263c78fac5a861
