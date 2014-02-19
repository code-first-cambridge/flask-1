# We're going to build the simplest possible web application using a tool
# called "flask".  To run this code, you'll need to have downloaded the flask
# library.
#
# First, you need to get hold of a tool called "pip".  pip is a tool that
# installs third-party Python libraries.  To install pip itslef, follow the
# instructions at http://pip.readthedocs.org/en/latest/installing.html.
# 
# Next, you can use pip to install flask.  From the command line, run
#
#   pip install flask
#
# This will produce a lot of output, but at the end you should see:
#
#   Successfully installed flask Werkzeug Jinja2 itsdangerous markupsafe
#   Cleaning up...
#
# To run this application from the command line, run
#
#   python hello1.py
#
# and then go to http://localhost:5000 to see your application in action.
#
# To stop the application running, from the command line press Ctrl-C.

# The flask module contains lots of things, but we only want to import
# something called *Flask*.
from flask import Flask

# We need to create an object that we can use to configure our application, and
# then to run it.  It doesn't matter what you call the object, but we usually
# call it *app*.  This line is a bit of "boilerplate" code that you'll see in
# every flask application.
app = Flask(__name__)

# We write functions that flask will call when it gets a request.  If the
# function returns a string, it'll be sent directly to the user's browser.
# This function will get called when the user makes a request for '/', that is,
# for the root url.
#
# Don't worry too much about the *@app.route* line right now -- we'll see more
# of this soon, and it'll make more sense with some more examples.
@app.route('/')
def hello():
    return 'Hello World!'

# Remember, this *if* statement ensures that the code beneath it only gets run
# if you run this program directly from the command line.  You will almost
# always see a line like this in Python code.
if __name__ == '__main__':
    # This calls the *run* function on the app object that we created earlier.
    # This will cause flask to spin up a webserver and start serving your
    # application.
    app.run()

# Task: change the return value of the *hello* function to give you a personal
# greeting.
