import json
from wsgiref.util import request_uri

import requests
from api_clients.base_client import BaseClient
from utils.utils import *


class UserList(BaseClient):
    __getAllUsers = '{base_url}/api/users?page=2'
    __getAllUsersNeg = '{base_url}/api/users?page=23'
    __getSingleUser = '{base_url}/api/users/2'
    __post_single_user = '{base_url}/api/users'
    __post_single_user_reqBody = '{ "name": "morpheus", "job": "lead" }'
    __post_single_user_reqBody_negative = read_file('json_files','post_single_user.json')

    def userReq_get_all_users(self):
        request_url = self.__getAllUsers.format(base_url=self._base_url)
        print_request(url=request_url, request_type='get')
        return requests.get(request_url)

    def userReq_get_all_users_another_number(self):
        request_url = self.__getAllUsersNeg.format(base_url=self._base_url)
        print_request(url=request_url, request_type='get')
        return requests.get(request_url)

    def userReq_get_single_user(self):
        request_url = self.__getSingleUser.format(base_url=self._base_url)
        print_request(url=request_url, request_type='get')
        return requests.get(request_url)

    def userReq_post_single_user(self):
        request_body = json.loads(self.__post_single_user_reqBody)
        request_url = self.__post_single_user.format(base_url=self._base_url)
        print_request(url=request_url, request_type='post')
        return requests.post(request_url,json=request_body)

    def userReq_post_single_user_negative(self):
        request_url = self.__post_single_user.format(base_url=self._base_url)
        req_body = self.__post_single_user_reqBody_negative
        print_request(url=request_url,request_body=req_body)
        return requests.post(request_url,json=req_body)