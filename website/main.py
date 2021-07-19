from flask import Flask, render_template, url_for
app = Flask(__name__) # this gets the name of the file so Flask knows it's name 
#random comment

@app.route("/")
def home():
    return render_template('home.html', subtitle='Home Page', text='This is the home page')

@app.route("/about")
def about():
    return render_template('about.html', subtitle='About us', text='Welcome to our about page')

@app.route("/ingredient")
def ingredient():
    return render_template('ingredient.html', subtitle='Enter Ingredients', text='Hello')

@app.route("/recipe")
def recipe():
    return render_template('recipe.html', subtitle='Enter a recipe', text='Find a Recipe')

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")