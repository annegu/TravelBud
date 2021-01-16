from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def homepage():
    """View function for Home Page."""
    return render_template("home.html")

@app.route("/add-course")
def addcourse():
    return render_template("add-course.html")

@app.route("/signup")
def signup():
    return render_template("signup.html")

@app.route("/login")
def login():
    return render_template("login.html")


if __name__ == "__main__":
    app.run()#debug=True