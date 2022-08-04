from utils.utils import *

import pytest
import json


@pytest.mark.gen3
@pytest.mark.dependency()
def test_get_all_users(user_list):
    response = user_list.userReq_get_all_users()
    print_response(response=response)
    assert response.status_code == 200
    json_response = json.loads(response.text)
    assert 'page' in json_response
    assert ('per_page' and 'total_pages') in json_response


@pytest.mark.negative
@pytest.mark.dependency()
def test_get_all_users_negative(user_list):
    response = user_list.userReq_get_all_users_another_number()
    print_response(response=response)
    assert response.status_code == 200


@pytest.mark.dependency()
def test_get_single_users(user_list):
    response = user_list.userReq_get_single_user()
    print_response(response=response)
    assert response.status_code == 200
    json_response = json.loads(response.text)
    assert 'support' in json_response


def test_post_single_user(user_list):
    response = user_list.userReq_post_single_user()
    print_response(response=response)
    json_response = json.loads(response.text)
    assert response.status_code == 201
    assert 'name' in json_response


def test_post_single_user_negative(user_list):
    response = user_list.userReq_post_single_user_negative()
    print_response(response=response)
    assert response.status_code == 404
