from flask import Flask

app = Flask(__name__)

# ----We handle url requests or https requests in between app and app.run----
# if you load one page with your enter key, you are making an http request
# with python you receive THAT request then allocate that request to particular HTML page!!


app.run(debug=True, port=5002)
