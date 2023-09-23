from flask import Flask, render_template

app = Flask(__name__)


# -------------------------------------------------------------------------------------#
# ----We handle url requests or https requests in between app and app.run----
# if you load one page with your enter key, you are making an http request
# with python you receive THAT request then allocate that request to particular HTML page!!
# -------------------------------------------------------------------------------------#

# home page is handled by ("/") request
@app.route("/")
def index():
    return render_template("index.html")


app.run(debug=True, port=5002)
