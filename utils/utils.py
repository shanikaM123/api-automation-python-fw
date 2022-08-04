# encoding: utf-8

import random
import string
import json
from pathlib import Path
import time

import pytest


def get_static_relationship_id():
    return 'worksfor'


def get_test_app_name(size):
    return 'test_automation_app_' + ''.join(random.choice(string.digits + string.ascii_uppercase) for i in range(size))


def get_non_existent_id():
    return '%s-%s-%s-%s-%s' % (''.join(random.choice(string.digits + string.ascii_uppercase) for i in range(8)),
                               ''.join(random.choice(string.digits + string.ascii_uppercase) for i in range(4)),
                               ''.join(random.choice(string.digits + string.ascii_uppercase) for i in range(4)),
                               ''.join(random.choice(string.digits + string.ascii_uppercase) for i in range(4)),
                               ''.join(random.choice(string.digits + string.ascii_uppercase) for i in range(12)))


def get_list_id_for_version_creation():
    return '017c49b5-009b-c078-1228-8fa528f3c48e'


def get_list_id_for_org_version_creation():
    return '017cbc62-66e5-ebf6-966b-6500b839f97a'


def print_request(url, request_type, params='', headers='', body=''):
    try:
        body = f'Request body: {json.dumps(body, indent=2)}\n' if body != '' else ''
    except:
        body = f'Request body: {body}\n' if body != '' else ''
    if params != '':
        params_string = '?'
        for key in params:
            params_string += f'{key}={params[key]}&'
        params = params_string[:-1]
    print(f'\nRequest: {request_type.upper()} {url}{params}\n{body}Request headers: {headers}\n')


def print_response(response):
    try:
        response_body = json.dumps(json.loads(response.text), indent=2)
    except:
        response_body = response.text
    print(f'Response code: {response.status_code}\nResponse body: {response_body}')


def get_clientId():
    return 'sparta_456w3034'


def read_file(folder_name, file_name):
    BASE_PATH = Path.cwd().joinpath('tests', 'resources')
    path = BASE_PATH.joinpath(folder_name, file_name)
    open_file = open(path, 'r')
    return json.loads(open_file.read())


def read_file_to_string(folder_name, file_name):
    BASE_PATH = Path.cwd().joinpath('tests', 'resources')
    path = BASE_PATH.joinpath(folder_name, file_name)
    print(path)
    open_file = open(path, 'r')
    return open_file.read()


def get_stat_workflow_screen_id():
    return '623ec6a6ce974f8ba3fed1076fde7787'
