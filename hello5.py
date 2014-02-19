# We want to return HTML to the browser, and not just plain text.  We could do
# that by joining strings together as this example shows.

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hello():
    html = '<!doctype html>' +\
           '<html>' +\
           '    <head>' +\
           '        <title>Hello</title>' +\
           '    </head>' +\
           '    <body>' +\
           '        <h1>Hello World!</h1>' +\
           '    </body>' +\
           '</html>'
    return html

@app.route('/hello/<name>')
def personalised_hello(name):
    html = '<!doctype html>' +\
           '<html>' +\
           '    <head>' +\
           '        <title>Hello</title>' +\
           '    </head>' +\
           '    <body>' +\
           '        <h1>Hello {0}!</h1>'.format(name) +\
           '    </body>' +\
           '</html>'
    return html

if __name__ == '__main__':
    app.run()

# Task: Google for "python multiline string" and find out how to slightly
# improve this example.
