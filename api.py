import requests
from dummy import dummy
import json
from recipe_info import recipe_info

headers = {
        'x-rapidapi-key': "b28cffec83msh01f2949c69f1af9p16ee98jsnb1cc8145b207",
        'x-rapidapi-host': "webknox-recipes.p.rapidapi.com"
        }


# User can search for recipes which utilize the ingredients they enter in. 
# Returns the Title, ID, image, and used/missing ingredients from the recipe.
def search_by_ingredient():
    url = "https://webknox-recipes.p.rapidapi.com/recipes/findByIngredients"
    user_input = input("Please enter the ingredients you have, separated by a comma.\n")
    querystring = {"ingredients":user_input,"number":"5"}

    #response = requests.request("GET", url, headers=headers, params=querystring)
    return parse_ingredient(dummy)


#Parses the search results of a call to search_by_ingredient
def parse_ingredient(file_name):
    new_dict = {}
    my_list = []
    num = 0
    for dict in file_name:
        new_dict['Title'] = dict['title']
        new_dict['Recipe ID'] = dict['id']
        new_dict['Image'] = dict['image']
        missing_list = []
        for ingredient in dict['missedIngredients']:
            missing_list.append(ingredient['original'])
            new_dict['Missing Ingredients'] = missing_list
        used_list = []
        for ingredient in dict['usedIngredients']:
            used_list.append(ingredient['original'])
            new_dict['usedIngredients'] = used_list
        my_list.append(new_dict.copy())
    return my_list


#call the API to obtain the recipe link given a food id
def my_recipe_info(food_id):
    url = "https://webknox-recipes.p.rapidapi.com/recipes/"+food_id+"/information"
    #response = requests.request("GET", url, headers=headers)
    return parse_recipe_info(recipe_info)


#Parses the search results of a call to my_recipe_info
def parse_recipe_info(file_name):
    return file_name["sourceUrl"]


if __name__ == '__main__':
    print(my_recipe_info("6262643"))
    