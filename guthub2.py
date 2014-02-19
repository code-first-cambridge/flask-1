# When running guthub1, try going to http://localhost:5000/sausages-and-mash.
# You should see generic error message.  It'd be better to give the user a more
# helpful error message.  To find out what's caused the error message, change
# the line:
#
#   app.run()
#
# to:
#
#   app.run(debug=True)
#
# Restart the app, and reload the page.  You should see some useful output
# about an error in our code.  Specifically, there's a KeyError on line 33.
# That's where we look up the recipe by its slug in the *recipes* dictionary.
# If you try to look up a key that's not present in a dictionary, Python raises
# a KeyError exception.  It's very easy to catch exceptions so that they don't
# cause a crash.

from flask import Flask, render_template

# We're now storing our recipes in a separate module so as to not clutter up
# the code.  We can import the *recipes* dictionary from that module.
from guthub_recipes import recipes

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', recipes=recipes)

@app.route('/recipe/<slug>')
def recipe(slug):
    try:
        # This next line might raise a KeyError.
        recipe = recipes[slug]
        # This line will only get run if the line above completes successfully.
        return render_template('recipe.html', recipe=recipe)
    except KeyError:
        # This code gets run if any code in the *try* block above raises a
        # KeyError.
        return render_template('recipe_not_found.html')

if __name__ == '__main__':
    app.run()

# Task: In the recipe_not_found template, display the slug that couldn't be
# found.
