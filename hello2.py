import datetime
from flask import Flask

app = Flask(__name__)

# Our first example did nothing that a static website couldn't do.  This time,
# we add the current time to the response.
@app.route('/')
def hello():
    # This is how you get the current time in Python.
    now = datetime.datetime.now().time()

    # We can substitute values into a string like this.
    return 'Hello World!  The time is: {0}'.format(now)

if __name__ == '__main__':
    app.run()

# Task: Read up on the datetime module in the Python docs online.