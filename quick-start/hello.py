from flask import Flask
from markupsafe import escape

"""
Code produced by following the Flask quickstart guide:
https://flask.palletsprojects.com/en/stable/quickstart/#a-minimal-application


This script creates a minimal Flask application. It imports the Flask class
from the flask module and creates an instance of the Flask class. The __name__
variable passed to the Flask class is a Python predefined variable, which is
set to the name of the module in which it is used. The Flask class uses this
argument to determine the root path of the application.

To run this application in debug mode in the browser on your
local machine, type/paste "flask --app quick-start/hello run --debug"
in the terminal and visit http://127.0.0.1:5000 with the appropriate route in
your browser. CTRL+C will stop the server.
"""

app = Flask(__name__)


@app.route("/")
def index():
    """Returns an 'Index' heading. Route is the root domain."""
    return "<h1>Index</h1>"

# Converter types:
# string - (default) accepts any text without a slash
# int - accepts positive integers
# float - accepts positive floating point values
# path - like string but also accepts slashes
# uuid - accepts UUID strings


@app.route("/hello")
def hello_world():
    """Returns a simple HTML string. Route is the /hello."""
    return "<p>Hello, World!</p>"


@app.route("/user/<string:name>")
def display_user_profile(name):
    """Return the user profile with the name escaped.
    Strings cannot contain slashes."""
    return f"<p>User {escape(name)}!</p>"


@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    """show the subpath after /path/ with slashes"""
    return f'Subpath {escape(subpath)}'


@app.route('/post/<int:post_id>')
def show_post(post_id):
    """show the post with the given id, the id is an integer"""
    return f'Post {post_id}'

# Canonical URLs and trailing slashes information:


@app.route('/projects/')
def projects():
    """
    The canonical URL for the projects endpoint has a trailing slash
    http://127.0.0.1:5000/projects/. It is similar to a folder in a file
    system. If you access the URL without a trailing slash
    http://127.0.0.1:5000/projects, Flask redirects you to the canonical URL
    with the trailing slash (/projects/).
    """
    return 'The project page'


@app.route('/about')
def about():
    """
    The canonical URL for the about endpoint does not have a trailing slash
    http://127.0.0.1:5000/about. It is similar to the pathname of a file.
    Accessing the URL with a trailing slash (http://127.0.0.1:5000/about/)
    produces a 404 “Not Found” error. This helps keep URLs unique for these
    resources, which helps search engines avoid indexing the same page twice.
    """
    return 'The about page'
