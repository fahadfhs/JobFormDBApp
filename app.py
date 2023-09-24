from flask import Flask, render_template, request

app = Flask(__name__)


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


app.run(debug=True, port=5002)
