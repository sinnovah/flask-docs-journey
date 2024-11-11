from flask import Flask
"""
Following the Flask quickstart guide:
https://flask.palletsprojects.com/en/stable/quickstart/#a-minimal-application


This script creates a minimal Flask application. It imports the Flask class
from the flask module and creates an instance of the Flask class. The __name__
variable passed to the Flask class is a Python predefined variable, which is
set to the name of the module in which it is used. The Flask class uses this
argument to determine the root path of the application.

To run this application in debug mode in the browser on your
local machine, type/paste "flask --app a-minimal-application/hello run --debug"
in the terminal and visit http://127.0.0.1:5000 with the appropriate route in
your browser. CTRL+C will stop the server.

Functions:
    hello_world(): Returns a simple HTML string "<p>Hello, World!</p>".
Routes:
    /: Visiting the root domain calls the hello_world function and returns
    its output.
"""

app = Flask(__name__)


@app.route("/")
def hello_world():
    """Returns a simple HTML string. Route is the root domain."""
    return "<p>Hello, World!</p>"
