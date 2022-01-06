from behave import *
from payLoad import *
from utilities.configurations import *
from utilities.resources import *
import requests


@given("the Book details which need to be added to Library")
def step_impl(context):

    context.add_url = getConfig()["API"]["endpoint"] + ApiResources.addBook
    context.headers = {"Content_Type": "application/json"}
    context.query = "SELECT * FROM Books"
    context.payload = buildPayLoadFromDB(context.query)


@when("we execute the AddBook PostPI method")
def step_impl(context):

    context.addBook_response = requests.post(
        context.add_url,
        json=context.payload,
        headers=context.headers,
    )


@then("book is successfully added")
def step_impl(context):

    print(context.addBook_response.json())
    response_addBook = context.addBook_response.json()
    assert "successfully added" in response_addBook["Msg"]
