# encoding: utf-8

import os
import pytest

from api_clients.get_allApplications import *
import configparser
import ast


def pytest_addoption(parser):
    parser.addoption("--user_list_base_url", action="store", default="none", help="user_list_base_url")


@pytest.fixture(scope='session')
def user_list(request):
    print('test')
    base_url = request.config.getoption("--user_list_base_url")
    print(base_url)
    if base_url == 'none':
        config = configparser.ConfigParser()
        config.read('config.properties')
        base_url = config['user_list']['user_list_base_url']
    return UserList(base_url=base_url)

