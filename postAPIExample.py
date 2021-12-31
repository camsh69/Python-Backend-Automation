import requests
from payLoad import addBookPayload
from utilities.configurations import getConfig
from utilities.resources import ApiResources

add_url = getConfig()['API']['endpoint'] + ApiResources.addBook
delete_url = getConfig()['API']['endpoint'] + ApiResources.deleteBook
headers = {"Content_Type": "application/json"}

addBook_response = requests.post(
    add_url, json=addBookPayload("bcd987"), headers=headers,)

print(addBook_response.status_code)
assert addBook_response.status_code == 200

print(addBook_response.json())
response_addBook = addBook_response.json()
assert "successfully added" in response_addBook["Msg"]

bookID = response_addBook['ID']

response_deleteBook = requests.post(delete_url, json={
    "ID": bookID
}, headers=headers,)

print(response_deleteBook.status_code)
assert response_deleteBook.status_code == 200

res_json = response_deleteBook.json()
print(res_json)
assert 'successfully deleted' in res_json['msg']
