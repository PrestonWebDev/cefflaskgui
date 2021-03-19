# These are the needed modules in order to render your UI
from flask import *
from cefflaskgui import *

# This initializes the app
app = Flask(__name__)

# This makes the / route and tells it to return hello world
@app.route("/")
def index():
	return "hello world"

# This sets all of the required variables
cefflaskgui.app = app
cefflaskgui.port = 5000
cefflaskgui.title = "test"

# This runs the GUI
cefflaskgui.run()