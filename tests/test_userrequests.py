from assertpy import assert_that
from cerberus import Validator

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


def test_post_register_unsuccessful(user_list):
    response = user_list.user_Req_post_register_unsuccessful()
    print_response(response=response)
    json_response = json.loads(response.text)
    assert response.status_code == 400
    error_value = json_response['error']
    assert error_value == 'Missing password'


def test_post_login_successful(user_list):
    response = user_list.user_Req_post_login_successful()
    json_response = json.loads(response.text)
    assert response.status_code == 200
    response_value = json_response['token']
    assert response_value == 'QpwL5tke4Pnpja7X4'

def test_delete_single_user(user_list):
    response = user_list.user_Req_delete_single_user()
    assert response.status_code == 204
