# encoding: utf-8

import os
import pytest

from api_clients.get_allApplications import *
import configparser
import ast


def pytest_addoption(parser):
    parser.addoption("--client_id", action="store", default="none", help="client_id")
    parser.addoption("--byos_workflow_base_url", action="store", default="none", help="byos_workflow_base_url")


@pytest.fixture(scope='session')
def be_byos(request):
    print('test')
    base_url = request.config.getoption("--byos_workflow_base_url")
    print(base_url)
    if base_url == 'none':
        config = configparser.ConfigParser()
        config.read('config.properties')
        base_url = config['be_byos']['byos_workflow_base_url']
    return Applications(base_url=base_url)

