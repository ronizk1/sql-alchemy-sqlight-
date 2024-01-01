from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
# Change the database URL to use SQLite
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///recipes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Recipe(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name_of_recipe = db.Column(db.String(45), nullable=False)
    ingredients = db.Column(db.String(45), nullable=False)
    prepare_time = db.Column(db.String(45), nullable=False)

# Create tables
# db.create_all()

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/list_recipes')
def index():
    with app.app_context():
        recipes = Recipe.query.all()
    return render_template('list_recipes.html', recipes=recipes)

@app.route('/add_recipe', methods=['GET', 'POST'])
def add_recipe():
    if request.method == 'POST':
        new_recipe = Recipe(
            name_of_recipe=request.form['name'],
            ingredients=request.form['ingredients'],
            prepare_time=request.form['prepare_time']
        )
        with app.app_context():
            db.session.add(new_recipe)
            db.session.commit()
            flash('Recipe added successfully', 'success')
        return redirect(url_for('index'))
    return render_template('add_recipe.html')

@app.route('/delete_recipe/<int:recipe_id>', methods=['GET'])
def delete_recipe(recipe_id):
    with app.app_context():
        recipe_to_delete = Recipe.query.get(recipe_id)
        if recipe_to_delete:
            db.session.delete(recipe_to_delete)
            db.session.commit()
            flash('Recipe deleted successfully', 'success')
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.secret_key = 'your_secret_key'  # Change this to a secret key for session management
    with app.app_context():
        db.create_all()
    app.run(debug=True)
