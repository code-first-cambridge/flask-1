from flask import Flask, render_template

app = Flask(__name__)

recipes = {
    'spaghetti-bolognese': {
        'name': 'Spaghetti Bolognese',
        'description': 'Spaghetti with a rich meaty sauce',
        'ingredients': ['spaghetti', 'mince', 'tomatoes', 'onions', 'garlic', 'cheese'],
        'instructions': 'Cook the pasta in boiling water.  Slowly fry the other ingredients until the meat is tender.  Garnish with grated cheese.',
    },
    'spaghetti-carbonara': {
        'name': 'Spaghetti Carbonara',
        'description': 'Spaghetti with a creamy bacony sauce',
        'ingredients': ['spaghetti', 'eggs', 'bacon', 'cheese'],
        'instructions': 'Cook the pasta in boiling water.  Separately, chop the bacon into small pieces and fry.  Once the pasta has cooked, mix the raw egg into the pasta and let it be cooked by the heat of the pasta.  Add the bacon and cheese, and serve.',
    },
    'eggs-florentine': {
        'name': 'Eggs Florentine',
        'description': 'Poached egg with salmon and spinach',
        'ingredients': ['eggs', 'muffins', 'salmon', 'spinach', 'sauce'],
        'instructions': 'Boil the spinach, poach the eggs, and layer together over half a muffin.  Drizzle with the sauce.',
    }
}

@app.route('/')
def index():
    return render_template('index.html', recipes=recipes)

@app.route('/recipe/<slug>')
def recipe(slug):
    recipe = recipes[slug]
    return render_template('recipe.html', recipe=recipe)

if __name__ == '__main__':
    app.run()

# Question: What happens if you look up a recipe that isn't in the database?
# Task: Add a link back to the index page from the bottom of each recipe page.
