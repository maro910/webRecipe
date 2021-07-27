import requests
#import json
import pandas as pd
#from similar_recip import similar

headers = {
        'x-rapidapi-key': "f888c871b1msh73f2e40214b8958p1399c0jsneedeb80a5574",
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
    response = parse_ingredient(requests.get(url, headers=headers, params=querystring).json()) 
    print(results)
    if results == []:
        return ("There were no results for the ingredients you chose. Please ensure that your spelling/format is correct and try again")
    #if the call was successful, return the results a dataframe
    return(results)

#Parses the search results of a call to search_by_ingredient
def parse_ingredient(file_name):
	new_dict = {}
	my_list = []
	num = 0
	for dict in file_name:
		new_dict['Title'] = dict['title']
		new_dict['Recipe ID'] = dict['id']
		new_dict['Image'] = dict['image']
		new_dict['Link'] = my_recipe_info(dict['id'])
		missing_list = []
		for ingredient in dict['missedIngredients']:
			missing_list.append(ingredient['original'])
			new_dict['Missing Ingredients'] = missing_list
		used_list = []
		for ingredient in dict['usedIngredients']:
			used_list.append(ingredient['original'])
			new_dict['Used Ingredients'] = used_list
		my_list.append(new_dict.copy())
	return my_list


#call the API to obtain the recipe link given a food id; used for search_by_ingredient b/c that endpoint does not return a link to the recipe
def my_recipe_info(food_id):
	food_id = str(food_id)
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
	results = requests.request("GET", url, headers=headers, params=querystring)
	if results == []:
		return "There were no results for the keywords you entered. Please ensure that your spelling/format is correct and try again"
	return (results)


#Parses the search results of a call to search_by_recipe
def parse_recipe_search(file_name):
	new_dict = {}
	my_list = []
	for recipe in file_name['results']:
		new_dict['Name'] = recipe['title']
		new_dict['Ready in'] = recipe['readyInMinutes']
		new_dict["Servings"] = recipe['servings']
		new_dict['Link'] = recipe['sourceUrl']
		new_dict['Recipe ID'] = recipe['id']
		new_dict['Image'] = recipe['image']
		my_list.append(new_dict.copy())
	return my_list


def similar_recipes():
	try:
		search_results = search_by_recipe()
		recipe_id = str(search_results[0]['Recipe ID'])
		url = "https://webknox-recipes.p.rapidapi.com/recipes/"+recipe_id+"/similar"
		response = requests.request("GET", url, headers=headers)
		results = parse_similar_recipes(response.json())
		if results == []:
			return ("There were no results for the recipe you chose. Please ensure that your spelling is correct and try again")
		return results
	except TypeError:
		return "The recipe you entered was not found. Please try another recipe"


def parse_similar_recipes(file_name):
	new_dict = {}
	my_list = []
	for recipe in file_name:
		new_dict['Title'] = recipe['title']
		new_dict['Ready in'] = recipe['readyInMinutes']
		new_dict['Servings'] = recipe['servings']
		new_dict['Link'] = recipe['sourceUrl']
		my_list.append(new_dict.copy())
	return my_list


if __name__ == '__main__':
    #print(search_by_ingredient())
	#print(my_recipe_info('ENTER RECIPE_ID HERE'))
	print(search_by_recipe())
	#search_by_ingredient()
	#print(similar_recipes())
	
