# We can make the HTML pages look a bit nicer by using a stylesheet.  In this
# case, we'll just use bootstrap's default styles.  Flask expects to find the
# stylesheets in the directory called "static".

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hello():
    return render_template('hello-styled.html', name='World')

@app.route('/hello/<name>')
def personalised_hello(name):
    return render_template('hello-styled.html', name=name)

if __name__ == '__main__':
    app.run()
