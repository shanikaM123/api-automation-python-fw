import requests
from api_clients.base_client import BaseClient
from utils.utils import *


class AuthorRequests(BaseClient):
    __get_authors = '{base_url}'
    __post_authors = '{base_url}'
    __post_authors_list_reqBody = read_file('json_files', 'post_authors_list.json')

    def get_author_list(self):
        request_url = self.__get_authors.format(base_url=self._base_url)
        print_request(url=request_url, request_type='get')
        return requests.get(request_url)

    def post_author_list(self):
        request_url = self.__post_authors.format(base_url=self._base_url)
        request_body = self.__post_authors_list_reqBody
        return requests.post(request_url, json=request_body)
