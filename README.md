# cefflaskgui
A python package for making advanced HTML, CSS, and JavaScript UIs for the desktop using flask and cefpython

---

## Table of contents
- **[Requirements](#Requirements)**
- **[Getting Started](#Getting-Started)**
- **[Conclusion](#Conclusion)**

---

<br/>
<br/>

## Requirements

- Python <= 3.7
- Cefpython => 66.0
- Flask latest version

<br/>
<br/>

---

<br/>
<br/>

## Getting Started

<br/>

**first off, create a new python script and name it whatever you want, I'll call mine `example.py`**

<br/>

#### **`example.py`**
``` python
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
```

### What does this all mean?
```python
# These are the needed modules in order to render your UI
from flask import *
from cefflaskgui import *
```
- Flask is needed so that you can make the server side app
- cefflaskgui is needed so you can render that app as a desktop app

<br/>

```python
# This initializes the app
app = Flask(__name__)

# This makes the / route and tells it to return hello world
@app.route("/")
def index():
	return "hello world"
```
- ```python
    app = Flask(__name__)
    ```
    - initializes a flask app

<br/>
<br/>

- ```python
    # This makes the / route and tells it to return hello world
    @app.route("/")
    def index():
        return "hello world"
    ```
    - This makes the / route, and has that route return the text hello world

<br/>

```python
    # This sets all of the required variables
    cefflaskgui.app = app
    cefflaskgui.port = 5000
    cefflaskgui.title = "test"
```
- This sets all of the required variables
- the cefflaskgui.app is just the app variable previouslyinitialized
- The cefflaskgui.port is the port you want your flask apprunning on
- The cefflaskgui.title is the title of your app

<br/>

```python
  # This runs the GUI
  cefflaskgui.run()
```
- cefflaskgui.run() runs the app

---

<br/>
<br/>

## Conclusion

<br/>

**This simple module multithreads Flask and Cefpython so you can create nice and advanced UIs. Unlike its competitors, flaskwebgui, and pyfladesk, this package uses Chromium Embedded to render HTML, CSS, and JavaScript. The issue with pyfladesk is that it is difficult to get links working, and flaskwebgui depends on the user having google chrome downloaded, whereas with cefflaskgui, since it uses Chromium embedded, it comes preinstalled with the renderer, and you can actually link to other pages and use the latest HTML, CSS, and JavaScript integration.**