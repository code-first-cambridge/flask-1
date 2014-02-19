# Our last example showed how tedious it can be to create HTML out of Python
# strings.  This example shows a better approach, using HTML template files.
# You need to have a directory called "templates".  In the current templates
# directory, you've got a file called hello.html, which has the following
# contents:
#
#    <!doctype html>
#    <html>
#        <head>
#            <title>Hello</title>
#        </head>
#        <body>
#            <h1>Hello {{ name }}!</h1>
#        </body>
#    </html>
#
# This is ordinary HTML, except for {{ name }}.  We're going to pass a name to
# the template, and flask will substitute it in here.

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hello():
    # Now, when we call *render_template*, we pass in a named argument -- in
    # this case it's called "name".  The corresponding value is used when flask
    # renders the template.
    return render_template('hello.html', name='World')

@app.route('/hello/<name>')
def personalised_hello(name):
    return render_template('hello.html', name=name)

if __name__ == '__main__':
    app.run()

# Task: View the source of the page in your browser to convince yourself of
# where the HTML is coming from.
