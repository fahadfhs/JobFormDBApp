from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config["SECRET_KEY"] = "myapplication123"
# below specifies that we're using sqlite database
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data.db"
db = SQLAlchemy(app)


class Form(db.Model):
    # creating the columns for the db
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(80))
    last_name = db.Column(db.String(80))
    email = db.Column(db.String(80))
    date = db.Column(db.Date)
    occupation = db.Column(db.String(80))


# -------------------------------------------------------------------------------------#
# ----We handle url requests or https requests in between app and app.run----
# if you load one page with your enter key, you are making an http request
# with python you receive THAT request then allocate that request to particular HTML page!!
# -------------------------------------------------------------------------------------#

# home page is handled by ("/") request

@app.route("/", methods=["GET", "POST"])
def index():
    print(request.method)
    if request.method == "POST":
        first_name = request.form["first_name"]
        last_name = request.form["last_name"]
        email = request.form["email"]
        date = request.form["date"]
        occupation = request.form["occupation"]

    return render_template("index.html")


if __name__ == "__main__":
    # creates a database after running the browser
    with app.app_context():
        db.create_all()
        app.run(debug=True, port=5002)
