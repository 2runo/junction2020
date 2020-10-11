import requests
import ast


def jsonify(string):
    string = string.replace('true', 'True')
    string = string.replace('false', 'False')
    string = string.replace('none', 'None')
    string = string.replace('null', 'None')
    string = string.replace('&amp;', '&')
    string = string.replace('&nbsp;', ' ')
    string = string.replace('&lt;', '<')
    string = string.replace('&gt;', '>')
    string = string.replace('&#035;', '#')
    return ast.literal_eval(string)


def us_restaurant_menus_request(lon, lat, distance=1):
    url = "https://us-restaurant-menus.p.rapidapi.com/restaurants/search/geo"

    querystring = {"lon":str(lon),"lat":str(lat),"distance":str(distance)}

    headers = {
        'x-rapidapi-host': "us-restaurant-menus.p.rapidapi.com",
        'x-rapidapi-key': "b385c0601dmsh4fb2f24b9b2d010p1ef59fjsna878b975f665"
        }

    response = requests.request("GET", url, headers=headers, params=querystring)
    string = response.text
    string = jsonify(string)
    data = string['result']['data']
    return data


def recipe_search_and_diet_request(q):
    url = "https://edamam-recipe-search.p.rapidapi.com/search"

    querystring = {"q": q}

    headers = {
        'x-rapidapi-host': "edamam-recipe-search.p.rapidapi.com",
        'x-rapidapi-key': "b385c0601dmsh4fb2f24b9b2d010p1ef59fjsna878b975f665"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)
    string = response.text
    string = jsonify(string)
    hits = string['hits']
    result = []
    for recipe in hits:
        result.append([recipe['recipe']['label']] + [ingredient['text'] for ingredient in recipe['recipe']['ingredients']])
    return result


if __name__ == "__main__":
    data = us_restaurant_menus_request(39.787947, -86.160467)
    print(data)
    result = recipe_search_and_diet_request("chicken")
    print(result)
