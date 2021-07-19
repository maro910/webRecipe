import requests
#123lljlkkljl
#random
url = "https://webknox-recipes.p.rapidapi.com/recipes/findByIngredients"

querystring = {"ingredients":"apples,flour,sugar","number":"5"}

headers = {
    'x-rapidapi-key': "b28cffec83msh01f2949c69f1af9p16ee98jsnb1cc8145b207",
    'x-rapidapi-host': "webknox-recipes.p.rapidapi.com"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)
