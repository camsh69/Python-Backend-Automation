import requests
import json
from utilities.configurations import getConfig
from utilities.resources import ApiResources

get_url = getConfig()['API']['endpoint'] + ApiResources.getBook
params = ApiResources.params

response = requests.get(get_url, params=params)

# *** using .text to return JSON string
# print(response.text)
# print(type(response.text))

# *** json.loads() method converts JSON to dictionary (or list of dictionaries)
# dict_response = json.loads(response.text)
# print(type(dict_response))
# print(dict_response[0]["isbn"])

# *** using .json() to turn JSON into dictionary (or list of dictionaries)
json_response = response.json()
# print(json_response)
print(type(json_response))
print(json_response[0]['isbn'])

# *** get status code
assert response.status_code == 200

# *** get headers
print(response.headers)
assert "application/json" in response.headers["Content-Type"]

# *** get cookies
print(response.cookies)

# *** retrieve specific value
for book in json_response:
    if book['isbn'] == 'Seyn':
        print(book['book_name'])
        break

assert book['book_name'] == 'Devops'
