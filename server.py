# python 3.7
import api
import firebase
from sanic import Sanic
from sanic.response import json
from sanic.response import text

app = Sanic("AskKey")

# us restaurant menus
@app.route("/us-restaurant-menus", methods=['GET'])
async def us_restaurant_menus_handler(request):
    req = request.args
    lon, lat = req['lon'][0], req['lat'][0]
    if 'distance' in req:
        distance = req['distance'][0]
    else:
        distance = 99999999

    inform = api.us_restaurant_menus_request(lon, lat, distance)[0]
    name = inform['restaurant_name']
    address = inform['address']['formatted']
    menu = firebase.get_menu(name)
    response = {"name": name, "address": address, "menu": menu}
    return json(response)

# recipe search and diet
@app.route("/recipe_search_and_diet", methods=['GET'])
async def recipe_search_and_diet_handler(request):
    req = request.args
    q = req['q'][0]

    recipe = api.recipe_search_and_diet_request(q)[0]
    name = recipe[0]
    recipe = recipe[1:]
    response = {"name": name, "recipe": recipe, "q": q}
    return json(response)

# 오류 핸들러
@app.exception(Exception)
async def exception_handler(request, exception):
    return text("Error {}".format(exception))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
