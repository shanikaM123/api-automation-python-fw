# encoding: utf-8

class BaseClient:
    _base_url = None
    _token = None
    _headers = {}

    def __init__(self, base_url):
        self._base_url = base_url
        self._headers['Content-Type'] = 'application/json'

