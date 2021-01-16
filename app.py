from flask import Flask, render_template
app = Flask(__name__)

COURSES = ["ece216","ece221","ece231","ece243","ece216","ece221","ece231","ece243"]


@app.route("/",  methods=["POST", "GET"])
def homepage():
    """View function for Home Page."""

    return render_template("coursePage.html", courseName = "Ece216",Courses = COURSES)

@app.route("/signup", methods=["POST", "GET"])
def signup():
    form = SignUpForm()
    return render_template("signup.html", form = form)


@app.route("/changePage",  methods=["POST", "GET"])
def changePage():
    """View function for Home Page."""

    return render_template("coursePage.html", courseName = "IT WORKEDDD")
class StudentCourseData:
  def __init__(self):
    self.labsCompleted = []
    self.PSCompleted = []

if __name__ == "__main__":
    app.run()#debug=True

class Assignment:
    def __init__(self, id, name, dueDate, worth):
        self.id = id
        self.name = name
        self.dueDate = dueDate
        self.classRating = 0
        self.numDone = 0

class Student: 
    def __init__(self, courses, courseData):
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
