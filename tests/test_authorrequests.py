from utils import *
import pytest
import json
from jsonschema import validate, Draft7Validator
from jsonschema import validators


def test_get_allAuthors(author_list):
    response = author_list.get_author_list()
    print(response)
    assert response.status_code == 200


def test_post_authors(author_list):
    response = author_list.post_author_list()
    print(response)
    json_response = json.loads(response.text)
    assert response.status_code == 200
    assert json_response["id"] == 0
    assert json_response["idBook"] == 0
    assert json_response["firstName"] == "string"
    assert json_response["lastName"] == "string"


def test_get_authors_byBook(author_list):
    response = author_list.get_authors_byBook()
    print(response)
    json_response = json.loads(response.text)
    assert response.status_code == 200
    # assert json_response["firstName"] == "First Name 1"


def test_put_authors_byBook(author_list):
    response = author_list.put_authors_byBook()
    print(response)
    assert response.status_code == 200


def test_delete_authors_byBook(author_list):
    response = author_list.delete_authors_byBook()
    print(response)
    assert response.status_code == 200
