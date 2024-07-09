import requests
from requests.exceptions import RequestException
from url_data import base_url, path


class BaseMethods:
    def __init__(self):
        self.base_url = base_url
        self.path = path

    def get_data(self, endpoint, headers=None):
        try:
            response = requests.get(f"{self.base_url}{self.path}{endpoint}", headers=headers)
            return response
        except RequestException:
            return None

    def post(self, endpoint, payload, headers=None):
        try:
            response = requests.post(f"{self.base_url}{self.path}{endpoint}", json=payload, headers=headers)
            return response
        except RequestException:
            return None

    def patch(self, endpoint, payload, headers=None):
        try:
            response = requests.patch(f"{self.base_url}{self.path}{endpoint}", json=payload, headers=headers)
            return response
        except RequestException:
            return None
