from flask import Flask, render_template,abort
import forms as f
import db
app = Flask(__name__)
app.config['SECRET_KEY'] = 'dfewfew123213rwdsgert34tgfd1234trgf'


COURSES = ["ece216","ece221","ece231","ece243","ece216","ece221","ece231","ece243"]
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
        new_user = {"id": len(users)+1, "full_name": form.full_name.data, "email": form.email.data, "password": form.password.data}
        users.append(new_user)
        return render_template("newCourse.html", message = "Successfully signed up")
    return render_template("newCourse.html", form = form)


@app.route("/changePage",  methods=["POST", "GET"])
def changePage():
    """View function for Home Page."""
    #print(request.id)
    return render_template("coursePage.html", courseName = "IT WORKEDDD",Courses = COURSES)

if __name__ == "__main__":
    app.run()#debug=True
