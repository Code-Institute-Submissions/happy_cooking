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
    return render_template("recipes.html")


@app.route('/my_recipes')
def my_recipes():
    return render_template("my_recipes.html")


@app.route('/login')
def login():
    return render_template("login.html")


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
            
            