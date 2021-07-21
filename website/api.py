import requests
import json
import pandas as pd

headers = {
        'x-rapidapi-key': "835ea1863cmsh8ec245f12ad64bap187695jsn701aabefa0f1",
        'x-rapidapi-host': "webknox-recipes.p.rapidapi.com"
        }


#Returns data in a dataframe
def make_df(data):
    df = pd.DataFrame(data)
    return df


# User can search for recipes which utilize the ingredients they enter in. 
# Returns the Title, ID, image, and used/missing ingredients from the recipe.
def search_by_ingredient():
	url = "https://webknox-recipes.p.rapidapi.com/recipes/findByIngredients"
	user_input = input("Please enter the ingredients you have, separated by a comma.\n")
	querystring = {"ingredients":user_input,"number":"5"}
	response = requests.request("GET", url, headers=headers, params=querystring)
	results = parse_ingredient(response.json())
	if results == []:
		return ("There were no results for the ingredients you chose. Please ensure that your spelling/format is correct and try again")
	#if the call was successful, return the results a dataframe
	return make_df(results)


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


#call the API to obtain the recipe link given a food id; used for search_by_ingredient b/c that endpoint does not return a link to the recipe
def my_recipe_info(food_id):
    url = "https://webknox-recipes.p.rapidapi.com/recipes/"+food_id+"/information"
    response = requests.request("GET", url, headers=headers)
    return parse_recipe_info(response.json())


#Parses the search results of a call to my_recipe_info
def parse_recipe_info(file_name):
	try:
		return file_name["sourceUrl"]
	except KeyError:
		return 'Not a valid recipe ID.'


# User can search for recipes by keyword
# Returns the Name, Cooking time, servings, link, and image.
def search_by_recipe():
	url = "https://webknox-recipes.p.rapidapi.com/recipes/search"
	user_input = input("Please enter what you would like to make in order to find recipes\n")
	querystring = {"query":user_input,"offset":"0","number":"10"}
	response = requests.request("GET", url, headers=headers, params=querystring)
	results = parse_recipe_search(response.json())
	if results == []:
		return "There were no results for the keywords you entered. Please ensure that your spelling/format is correct and try again"
	return make_df(results)


#Parses the search results of a call to search_by_recipe
def parse_recipe_search(file_name):
	new_dict = {}
	my_list = []
	for recipe in file_name['results']:
		new_dict['Name'] = recipe['title']
		new_dict['Ready in'] = recipe['readyInMinutes']
		new_dict["Servings"] = recipe['servings']
		new_dict['Link'] = recipe['sourceUrl']
		new_dict['Image'] = recipe['image']
		my_list.append(new_dict.copy())
	return my_list
		

if __name__ == '__main__':
    #print(search_by_ingredient())
	#print(my_recipe_info('ENTER RECIPE_ID HERE'))
	#print(search_by_recipe())
	pass

