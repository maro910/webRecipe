from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm
from flask_behind_proxy import FlaskBehindProxy


app = Flask(__name__) # this gets the name of the file so Flask knows it's name 
proxied = FlaskBehindProxy(app)
app.config['SECRET_KEY'] = '18d37da1eb2f66efb3bceaf848905c93'
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

@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit(): # checks if entries are valid
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home')) # if so - send to home page
    return render_template('register.html', title='Register', form=form)

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")