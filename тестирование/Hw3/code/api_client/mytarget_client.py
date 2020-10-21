import json
from urllib.parse import urljoin
import requests


class ResponseStatusCodeException(Exception):
    pass


class RequestErrorException(Exception):
    pass


class MyTargetClient:
    def __init__(self, url, login, password):
        self.base_url = url
        self.login = login
        self.password = password
        self.session = requests.Session()
        self.authorization()
        csrf_token = None

    def _request(self, method, location, headers=None, params=None, data=None, json=False):
        if str(location).startswith('http'):
            url = location
        else:
            url = urljoin(self.base_url, location)

        response = self.session.request(method, url, headers=headers, params=params, data=data, allow_redirects=False)

        if json:
            json_response = response.json()

            if json_response.get('bStateError'):
                error = json_response['sErrorMsg']
                raise RequestErrorException(f'Request "{url}" dailed with error "{error}"!')
            return json_response
        return response

    def get_token(self):
        location = 'csrf'
        # решить с headers
        # headers = None
        headers = {
            'Referer': 'https://target.my.com/auth/mycom?state=target_login%3D1%26ignore_opener%3D1'
        }
        response_for_csrf = self._request('GET', location, headers=headers)
        token = response_for_csrf.headers['set-cookie'].split(';')[0].split('=')[-1]
        return token

    def authorization(self):
        location = 'https://auth-ac.my.com/auth?lang=ru&nosavelogin=0'
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded',
            'Origin': 'https://target.my.com',
            'Referer': 'https://target.my.com/'
        }

        data = {
            'email': self.login,
            'password': self.password,
            'continue': 'https://target.my.com/auth/mycom?state=target_login%3D1%26ignore_opener%3D1#email',
            'failure': 'https://account.my.com/login/'
        }

        response = self._request('POST', location, headers=headers, data=data, json=False)
        while response.status_code != 200:
            response = self._request('GET', response.headers['Location'])

        self.csrf_token = self.get_token()
        return response

    def create_segment(self, name):
        location = 'api/v2/remarketing/segments.json?fields=relations__object_type,relations__object_id,' \
                   'relations__params,relations_count,id,name,pass_condition,created,campaign_ids,users,flags '

        headers = {
            'X-CSRFToken': self.csrf_token
        }

        data = {
            "name": f"{name}",
            "pass_condition": 1,
            "relations": [{"object_type": "remarketing_player",
                           "params": {"type": "positive", "left": 365, "right": 0}},
                          {"object_type": "remarketing_payer",
                           "params": {"type": "positive", "left": 365, "right": 0}}],
            "logicType": "or"
        }
        data_for_upload = json.dumps(data)
        self._request('POST', location, headers=headers, data=data_for_upload)

    def delete_segment(self, name):
        id = self.convert_name_to_id(name)
        location = 'api/v1/remarketing/mass_action/delete.json'
        data = [{"source_id": id, "source_type": "segment"}]
        headers = {
            'Content-Type': 'application/json',
            'X-CSRFToken': self.csrf_token
        }
        data_for_upload = json.dumps(data)
        self._request('POST', location, headers=headers, data=data_for_upload)

    def check_segment_existence(self, name):
        counter = 0
        location = 'api/v2/remarketing/segments.json'
        response = self._request('Get', location, json=True)
        list_of_segments = response['items']
        for item in list_of_segments:
            if item.get('name') == str(name):
                counter += 1
        if counter:
            return True
        else:
            return False

    def convert_name_to_id(self, name):
        id_by_name = 0
        location = 'api/v2/remarketing/segments.json'
        response = self._request('Get', location, json=True)
        list_of_segments = response['items']
        for item in list_of_segments:
            if item.get('name') == str(name):
                id_by_name = item.get('id')
        return id_by_name
