import requests
from api_clients.base_client import BaseClient
from utils.utils import *


class AuthorRequests(BaseClient):
    __get_authors = '{base_url}'
    __post_authors = '{base_url}'
    __get_authors_byBook = '{base_url}/authors/books/1'
    __post_authors_list_reqBody = read_file('json_files', 'post_authors_list.json')
    __put_authors_byBook_reqBody = read_file('json_files', 'put_authors_list.json')
    __put_authors_byBook = '{base_url}/1'
    __delete_authors_byBook = '{base_url}/1'

    def get_author_list(self):
        request_url = self.__get_authors.format(base_url=self._base_url)
        print_request(url=request_url, request_type='get')
        return requests.get(request_url)

    def post_author_list(self):
        request_url = self.__post_authors.format(base_url=self._base_url)
        request_body = self.__post_authors_list_reqBody
        return requests.post(request_url, json=request_body)

    def get_authors_byBook(self):
        request_url = self.__get_authors_byBook.format(base_url=self._base_url)
        return requests.get(request_url)

    def put_authors_byBook(self):
        request_url = self.__put_authors_byBook.format(base_url=self._base_url)
        request_body = self.__put_authors_byBook_reqBody
        return requests.put(request_url,json=request_body)

    def delete_authors_byBook(self):
        request_url = self.__delete_authors_byBook.format(base_url=self._base_url)
        return requests.delete(request_url)