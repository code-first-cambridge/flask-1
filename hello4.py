from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello World!'

# We can add parameters to the URL.  In this case, Flask will use
# *personalised_hello* to handle any request to a url that looks like
# "/hello/Peter".
@app.route('/hello/<name>')
def personalised_hello(name):
    return 'Hello {0}!'.format(name)

if __name__ == '__main__':
    app.run()
