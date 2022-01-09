from behave import *
from payLoad import *
from utilities.configurations import *
from utilities.resources import *
import requests


@given("the Book details which need to be added to Library")
def step_impl(context):

    context.add_url = getConfig()["API"]["endpoint"] + ApiResources.addBook
    context.headers = {"Content_Type": "application/json"}
    context.payload = addBookPayload("dhavlf", "654")


@when("we execute the AddBook PostPI method")
def step_impl(context):

    context.response = requests.post(
        context.add_url,
        json=context.payload,
        headers=context.headers,
    )


@then("book is successfully added")
def step_impl(context):

    print(context.response.json())
    response_json = context.response.json()
    context.bookId = response_json["ID"]
    assert "successfully added" in response_json["Msg"]


@given("the Book details with {isbn} and {aisle}")
def step_impl(context, isbn, aisle):
    context.add_url = getConfig()["API"]["endpoint"] + ApiResources.addBook
    context.headers = {"Content_Type": "application/json"}
    context.payload = addBookPayload(isbn, aisle)


@given("I have github auth credentials")
def step_impl(context):
    context.se = requests.session()
    context.se.auth = auth = ("camsh69", "password")


@when("I hit getRepo of github")
def step_impl(context):
    context.response = context.se.get(ApiResources.githubRepo)


@then('status code of response is "{statusCode:d}"')
def step_impl(context, statusCode):
    print(context.response.status_code)
    assert context.response.status_code == statusCode
