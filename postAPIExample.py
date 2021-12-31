import requests
from payLoad import *

addBook_response = requests.post('http://216.10.245.166/Library/Addbook.php',
                                 json=addBookPayload("bcd989"), headers={"Content_Type": "application/json"},)

print(addBook_response.status_code)
assert addBook_response.status_code == 200

print(addBook_response.json())
response_addBook = addBook_response.json()
assert "successfully added" in response_addBook["Msg"]

bookID = response_addBook['ID']
response_deleteBook = requests.post('http://216.10.245.166/Library/DeleteBook.php', json={
    "ID": bookID
}, headers={"Content_Type": "application/json"},)
print(response_deleteBook.status_code)
assert response_deleteBook.status_code == 200

res_json = response_deleteBook.json()
print(res_json)
assert 'successfully deleted' in res_json['msg']
