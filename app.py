from flask import Flask, render_template
import db
app = Flask(__name__)

COURSES = ["ece216","ece221","ece231","ece243","ece216","ece221","ece231","ece243"]
stud = db.Student()

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
    #print(request.id)
    return render_template("coursePage.html", courseName = "IT WORKEDDD")

if __name__ == "__main__":
    app.run()#debug=True
