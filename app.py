import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)

app.config["MONGO_DBNAME"] = 'happy_cooking'
app.config["MONGO_URI"] = 'mongodb+srv://nellie10:Anything10@cluster0-ryuq4.mongodb.net/happy_cooking?retryWrites=true'

mongo = PyMongo(app)



@app.route('/')
def index():
    return render_template("index.html")
    
@app.route('/recipes')
def recipes():
    return render_template("recipes.html",
                            recipes=mongo.db.recipes.find())


@app.route('/my_recipes')
def my_recipes():
    return render_template("my_recipes.html",
     
                            my_recipes=mongo.db.my_recipes.find())

@app.route('/insert_recipe', methods=['POST'])
def insert_recipe ():
    recipes = mongo.db.recipes
    recipes.insert_one(request.form.to_dict())
    return redirect(url_for('recipes'))
    
@app.route('/edit_recipe/<recipe_id>')
def edit_recipe(recipe_id):
    the_recipe =  mongo.db.tasks.find_one({"_id": ObjectId(recipe_id)})
    all_my_recipes =  mongo.db.my_recipes.find()
    return render_template('edit_recipe.html', recipe=the_recipe,
                           my_recipes=all_my_recipes)

    

@app.route('/login')
def login():
    return render_template("login.html")

@app.route('/add_recipe')
def add_recipe():
    return render_template("add_recipe.html")

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)