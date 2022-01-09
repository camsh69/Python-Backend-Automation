import requests
from utilities.configurations import getConfig
from utilities.resources import ApiResources

delete_url = getConfig()["API"]["endpoint"] + ApiResources.deleteBook
headers = {"Content_Type": "application/json"}


def after_scenario(context, scenario):
    if "library" in scenario.tags:

        response_deleteBook = requests.post(
            delete_url,
            json={"ID": context.bookId},
            headers=headers,
        )

        print(response_deleteBook.status_code)
        assert response_deleteBook.status_code == 200

        res_json = response_deleteBook.json()
        print(res_json)
        assert "successfully deleted" in res_json["msg"]
