import datetime
from flask import Flask

app = Flask(__name__)

# A web application will normally respond to requests on lots of different
# URLs.  Flask lets us write different functions for handling different kinds
# of requests.  To do this, we "decorate" our function definitions with
# *app.route(some_url)*.  This is best demonstrated by example.

# Flask will call the function called *hello* when it receives a request for
# '/'.
@app.route('/')
def hello():
    return 'Hello World!'

# Flask will call the function called *current_time* when it receives a request
# for '/time'.
@app.route('/time')
def current_time():
    now = datetime.datetime.now().time()
    return 'Hello World!  The time is: {0}'.format(now)

if __name__ == '__main__':
    app.run()

# Question: What happens if you go to a URL in your browser that flask doesn't
# know about?
