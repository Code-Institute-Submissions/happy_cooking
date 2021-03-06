import os
from flask import Flask, render_template, redirect, request, url_for, session, escape, request
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from bson import json_util
import json
import datetime

app = Flask(__name__)

app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')
app.config["MONGO_DBNAME"] = 'happy_cooking'
app.config["MONGO_URI"] = os.environ.get('MONGO_URI')

mongo = PyMongo(app)


@app.route('/')
def index():
    return render_template("index.html")
    
@app.route('/recipes')
def recipes():
    
    cuisine =request.args.get("cuisine")
    allergen = request.args.get("allergen")
    query = {}
    if cuisine:
        query["meal"] = cuisine
    if allergen:
        query["allergen"] = {"$in": [ allergen]}
    recipes = mongo.db.recipes.find(query)

    recipes = sorted(
        recipes,
        key=lambda d: str(d.get('createdAt',datetime.datetime.now())),
        reverse=True
    )

    cuisines_json = json.loads(open('data/cuisine.json').read())
    allerges_json = json.loads(open('data/allergen.json').read())
    return render_template("recipes.html", recipes=recipes,cuisines_json=cuisines_json,allerges_json=allerges_json)
    



@app.route('/my_recipes')
def my_recipes():
    if session:
        return render_template("my_recipes.html", 
            my_recipes=mongo.db.my_recipes.find())
    else:
        return ('Login first!')               



@app.route('/insert_recipe', methods=['POST'])
def insert_recipe ():
    
    recipes = mongo.db.recipes
    (request.form.to_dict())
    (request.form.to_dict())
    recipes.insert_one({
        "createdAt": datetime.datetime.now(), 
        "name": request.form['recipe_name'], 
        "ingredients":request.form['recipe_ingredients'],     
        "instructions":request.form.get('recipe_instructions'),
        "cooking_time":request.form.get('cooking_time'),
        "author":request.form.get('recipe_author'),
        "meal":request.form.get('meal'),
        "dietary_requirement":request.form.get('dietary_requirement'),
        "serves":request.form.get('serves'),
    })
    return redirect(url_for('recipes'))
    
@app.route('/edit_recipe/<recipe_id>')
def edit_recipe(recipe_id):
    the_recipe =  mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    all_my_recipes =  mongo.db.recipes.find({"username": session['username']})
    return render_template('edit_recipe.html', recipe=the_recipe,
                           my_recipes=all_my_recipes)
                           
@app.route('/update_recipe/<recipe_id>', methods=['GET', 'POST'])
def update_recipe(recipe_id):
    if request.method == 'POST':
        (request.form.to_dict())
        mongo.db.recipes.update_one(
            {"_id":  ObjectId(recipe_id)},
                {
                    "$set": {
                        "name": request.form['recipe_name'],
                        "ingredients":request.form['recipe_ingredients'],
                        "recipe_method":request.form.get('recipe_instructions'),
                        "cooking_time":request.form.get('cooking_time'),
                        "author":request.form.get('recipe_author'),
                        "meal":request.form.get('meal'),
                        "dietary_requirement":request.form.get('dietary_requirement')
                    }
            })
        
        the_recipe =  mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
        return render_template("detail.html", recipe=the_recipe)

    
@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        user = mongo.db.users.find_one({
            'username': username
        })
        ("username here: " + json.dumps(list(user)))
        if user:
            if user['password'] == password:
                session['username'] = username
                return redirect(url_for('my_recipes'))
            else:
                return ('Incorrect username or password')
        else:
            return ('Invalid username or password')
        return render_template("login.html")
    else:
        return redirect(url_for('index'))    
    

@app.route('/detail')
def detail():
    action = request.args.get('action')
    recipe = request.args.get('recipe')
    cuisines_json = json.loads(open('data/cuisine.json').read())
    allerges_json = json.loads(open('data/allergen.json').read())
    the_recipe =  mongo.db.recipes.find_one({"_id": ObjectId(recipe)})
    if action == 'detail':
        (the_recipe)
        return render_template("detail.html", recipe=the_recipe,cuisines_json=cuisines_json,allerges_json=allerges_json)
    elif action == 'edit':
        return render_template("edit_recipe.html", recipe=the_recipe,cuisines_json=cuisines_json,allerges_json=allerges_json)
    elif action == 'delete':
        mongo.db.recipes.delete_one({"_id": ObjectId(recipe)})
        recipes = mongo.db.recipes.find({})
        return render_template("recipes.html", recipes=recipes,cuisines_json=cuisines_json,allerges_json=allerges_json)
        

@app.route('/add_recipe')
def add_recipe():
    return render_template("add_recipe.html")
    
@app.route('/logout')
def logout():
    # remove the username from the session if it's there
    session.pop('username', None)
    return redirect(url_for('index'))
        

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)