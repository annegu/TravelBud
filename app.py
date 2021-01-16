from flask import Flask, render_template,abort
import forms as f
import db
app = Flask(__name__)
app.config['SECRET_KEY'] = 'dfewfew123213rwdsgert34tgfd1234trgf'


COURSES = ["ece216","ece221","ece231","ece243","ece216","ece221","ece231","ece243"]
COURSE_OBJS = []
stud = db.Student()

@app.route("/")
def homepage():
    """View function for Home Page."""

    return render_template("coursePage.html", courseName = "Ece216",Courses = COURSES)

@app.route("/signup", methods=["POST", "GET"])
def signup():
    form = f.SignUpForm()
    if form.validate_on_submit():
        new_user = {"id": len(users)+1, "full_name": form.full_name.data, "email": form.email.data, "password": form.password.data}
        users.append(new_user)
        return render_template("signup.html", message = "Successfully signed up")
    return render_template("signup.html", form = form)

@app.route("/newCourse", methods=["POST", "GET"])
def newCourse():
    form = f.addNewCourse()
    if form.validate_on_submit():
        #
        # form.courseCode.data
        #form.numLabs.data
        # form.numPS.data
        #form.numLectures.data
        COURSE_OBJS.append(db.Course(form.courseCode.data, form.numLabs.data, form.numLectures.data, form.numPS.data))
        COURSES.append(form.courseCode.data)
        COURSE_OBJS[0].createLabsList()
        
        stud.addCourse(COURSE_OBJS[0].courseCode)
        stud.courses[0][1].addLab(4)


        return render_template("home.html", message = "Successfully signed up")
    return render_template("newCourse.html", form = form)


@app.route("/course/<curCourse>",  methods=["POST", "GET"])
def changePage(curCourse):
    """View function for Home Page."""
    return render_template("coursePage.html", courseName = curCourse,Courses = COURSES)

if __name__ == "__main__":
    app.run()#debug=True
