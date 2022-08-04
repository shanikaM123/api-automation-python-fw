import json

import requests
from api_clients.base_client import BaseClient
from utils.utils import *


class Applications(BaseClient):
    __getAllApplications = '{base_url}/api/users?page=2'

    def be_byos_get_all_application(self):
        request_url = self.__getAllApplications.format(base_url=self._base_url)
        print_request(url=request_url, request_type='get')
        return requests.get(request_url)
