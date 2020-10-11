import requests

res = requests.get('http://158.247.212.202:8000/us-restaurant-menus', params={'lon': '39.787947', 'lat': '-86.160467'})
print(res.text)


res = requests.get('http://158.247.212.202:8000/recipe_search_and_diet', params={'q': 'Egg Toast'})
print(res.text)
