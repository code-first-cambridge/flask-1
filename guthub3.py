# Challenge: Extend the GutHub application so that, given an ingredient, you
# can find out what recipes you can use it in.  You'll want to create a
# template for showing the ingredient and its recipes, and you'll want to fill
# out the ingredient function below.  You might also want to display a list of
# ingredients on the index page.

from flask import Flask, render_template

from guthub_recipes import recipes

ingredients = {
    'spaghetti': { 'recipes': ['spaghetti-bolognese', 'spaghetti-carbonara'] },
    'mince': { 'recipes': ['spaghetti-bolognese'] },
    'tomatoes': { 'recipes': ['spaghetti-bolognese'] },
    'onions': { 'recipes': ['spaghetti-bolognese'] },
    'garlic': { 'recipes': ['spaghetti-bolognese'] },
    'cheese': { 'recipes': ['spaghetti-bolognese', 'spaghetti-carbonara'] },
    'eggs': { 'recipes': ['spaghetti-carbonara', 'eggs-florentine'] },
    'bacon': { 'recipes': ['spaghetti-carbonara'] },
    'muffins': { 'recipes': ['eggs-florentine'] },
    'salmon': { 'recipes': ['eggs-florentine'] },
    'spinach': { 'recipes': ['eggs-florentine'] },
    'sauce': { 'recipes': ['eggs-florentine'] },
}

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', recipes=recipes, ingredients=ingredients)


@app.route('/recipe/<slug>')
def recipe(slug):
    try:
        recipe = recipes[slug]
        return render_template('recipe.html', recipe=recipe)
    except KeyError:
        return render_template('recipe_not_found.html')


@app.route('/ingredient/<slug>')
def ingredient(slug):
    return slug


if __name__ == '__main__':
    app.run()

# Extended challenge: It's tedious and error-prone to have to work out the
# value of the *ingredients* dictionary by hand.  Compute it based on the value
# of *recipes* instead.
