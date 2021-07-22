from flask import Flask, render_template, url_for, flash, redirect, request
import pandas as pd
import numpy as np
import requests
import api



# this gets the name of the file so Flask knows it's name 
app = Flask(__name__) 


# Authenication keys
headers = {
        'x-rapidapi-key': "835ea1863cmsh8ec245f12ad64bap187695jsn701aabefa0f1",
        'x-rapidapi-host': "webknox-recipes.p.rapidapi.com"
        }


# Home Page
@app.route("/")
def home():
    return render_template('home.html', subtitle='Home Page', text='This is the home page')

# About Page
@app.route("/about")
def about():
    return render_template('about.html', subtitle='About us', text='Welcome to our about page')

# Ingredient Page
@app.route("/ingredient", methods=["POST", "GET"])
def ingredient():
    url = "https://webknox-recipes.p.rapidapi.com/recipes/findByIngredients"
    
    # If user enters form, run this code
    if request.method == "POST":
        # Creates a string based on user input
        userString = ""
        for i in range(4):
            string = "variable" + str(i)
            user = request.form[string]
            userString += user + ","
            
        # Removes extra comma
        finalString = userString[:-1]
        
        # Passes in ingredients for API call
        querystring = {"ingredients":finalString,"number":"5"} 
        
        # Makes API call, stores it into a dictionary, and parses the info we need
        results = api.parse_ingredient(requests.get(url, headers=headers, params=querystring).json())
        
        #If no results show up
        if results == []:
            return "There were no results for the ingredients you chose. Please ensure that your spelling/format is correct and try again"
        
        df = pd.DataFrame(results)
        finalDf = df.to_string()
        
        #Renders final html and passes in data we called for
        return render_template('ingResults.html', usr=finalDf)
    
    #If user accesses this page, render ingredient page
    return render_template('ingredient.html')

# Recipe Page
@app.route("/recipe", methods=["POST", "GET"])
def recipe():
    url = "https://webknox-recipes.p.rapidapi.com/recipes/search"
    
    # If user enters form, run this code
    if request.method == "POST":
        # Stores user input and passes it into API param
        user_input = request.form["variable"]
        querystring = {"query":user_input,"offset":"0","number":"10"}
        
        # Makes API call, stores it into a dictionary, and parses the info we need
        results = api.parse_recipe_search(requests.get(url, headers=headers, params=querystring).json())
        
        # If no results show up
        if results == []:
            return "There were no results for the keywords you entered. Please ensure that your spelling/format is correct and try again"
        
        #Renders final html and passes in data we called for
        return render_template('recResults.html', results=results)
    
    #If user accesses this page, render recipe page
    return render_template('recipe.html')


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")
