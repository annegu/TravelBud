import random 
from flask import Flask, render_template,abort,redirect
import forms as f
import db
app = Flask(__name__)
app.config['SECRET_KEY'] = 'dfewfew123213rwdsgert34tgfd1234trgf'
 
users =[]

logged_in_user = -1

COURSES = []
COURSE_OBJS = []
stud = db.Student()
studData = db.StudentCourseData()
 
#Homepage show login info
@app.route("/")
def homepage():
    """View function for Home Page."""
    if(logged_in_user == -1):
        return redirect("/signin")

    return render_template("homePage.html",courseName = "Welcome", Courses = COURSES, blank = 1, curUser = users[logged_in_user])
 
@app.route("/signin", methods=["POST", "GET"])
def signin():
    form = f.LoginForm()
    if form.validate_on_submit():
        for user in users: 
            if form.email.data in user["email"] and form.password.data == user["password"]:
                 return redirect("/")               
 
    return render_template("login.html", form = form)
 
 
 
@app.route("/signup", methods=["POST", "GET"])
def signup():
    form = f.SignUpForm()
    if form.validate_on_submit():
        new_user = {"id": len(users), "full_name": form.full_name.data, "email": form.email.data, "password": form.password.data}
        users.append(new_user)
        print(new_user)
        global logged_in_user
        logged_in_user = new_user["id"]
        print("new user is ", logged_in_user)

        # NEW CHANGE
        # return redirect("/")
        return redirect("/phoneAuthentication")
    return render_template("signup.html", form = form)

# NEW CHANGE
@app.route("/phoneAuthentication", methods=["POST", "GET"])
def phoneAuthentication():
    form=f.phoneAuthenticationForm()
    if form.validate_on_submit():
        return redirect("/verify")
    return render_template("phoneAuthentication.html", form = form)

# NEW CHANGE
@app.route("/verify", methods=["POST", "GET"])
def verify():
    form=f.verify()
    if form.validate_on_submit():
        return redirect("/")
    return render_template("verify.html", form=form)
 
@app.route("/newCourse", methods=["POST", "GET"])
def newCourse():
    form = f.addNewCourse()
    if form.validate_on_submit():
        # form.courseCode.data
        #form.numLabs.data
        # form.numPS.data
        #form.numLectures.data
        COURSE_OBJS.append(db.Course(form.courseCode.data, form.numLabs.data, int(form.numLectures.data), form.numPS.data))
        COURSES.append(form.courseCode.data)
        
        for courseObj in COURSE_OBJS:
            if form.courseCode.data == courseObj.courseCode:
                courseObj.createLabsList()
                courseObj.createPSetsList()
                courseObj.createLecturesList()
        
        return redirect("/course/" + form.courseCode.data)
        # return redirect("/")
    return render_template("newCourse.html", form = form, Courses = COURSES)  
 
 
#User looks for courses to 'enroll' if not created prompts user to create the class
# @app.route("/findCourse", methods=["POST", "GET"])
# def findCourse():
#     form = f.findCourse()
#     if form.validate_on_submit():
#         #find the course
#         for cCode in COURSES:
#             if cCode == form.courseCode.data:
#                 return redirect("/course/" + form.courseCode.data)
        
#         return redirect("/newCourse")
 
#     return render_template("joinCourse.html", form = form,Courses = COURSES)
 
 
# @app.route("/course/<curCourse>",  methods=["POST", "GET"])
# def changePage(curCourse):
#     print()
#     for course in COURSE_OBJS:
#         if curCourse == course.courseCode:
#             labs = course.labs
#             assignments = course.problemSets
#             lectures = course.lectures
#             sendCourse = course
#             studass = [x for x,y in studData.PSCompleted]
#             studlec =  [x for x,y in studData.lecsCompleted]
#             studlab= [x for x,y in studData.labsCompleted]
#             rlab = [y for x,y in studData.labsCompleted]
#             rlec = [y for x,y in studData.lecsCompleted] 
#             rass =[y for x,y in studData.PSCompleted]                

#             return render_template("coursePage.html", courseName = curCourse, Courses = COURSES, Labs = labs, Assignments = assignments, Lectures = lectures, Course = sendCourse,
#                 Student = stud, studLab = studlab,studAss = studass,studLec = studlec, 
#                 rLab = rlab, rLec = rlec, rAss = rass, ran = ran[int(curCourse[3:]):])
 
#     return "NOT A VALID COURSE"
 
# @app.route("/rate/<curCourse>/<assType>/<assNum>/<rating>",  methods=["POST", "GET"])
# def rate(curCourse,assType,assNum,rating):  
#     #COURSES.append("IT WORKEDDDD LETS GOOO")
#     #mark assignment as complete
#     #Update rating
    
    
#     for course in COURSE_OBJS:
#         if curCourse == course.courseCode:
#             if assType == "lab":
#                 studData.addLab(rating)
#                 stud.addCourse(curCourse, studData)
#                 return redirect("/course/" + curCourse)

#             elif assType == "ass":
#                 studData.addPS(rating)
#                 stud.addCourse(curCourse, studData)
#                 return redirect("/course/" + curCourse)
            
#             else: 
#                 studData.addLec(rating)
#                 stud.addCourse(curCourse, studData)
#                 return redirect("/course/" + curCourse)

    # return redirect("/course/" + curCourse)
    # return render_template("coursePage.html", Student = stud, StudentData = studData)

if __name__ == "__main__":
    app.run()