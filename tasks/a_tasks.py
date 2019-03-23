from wrappers.http_client import HTTPWrappers


class ATasks():

    def __init__(self, client):
        self.client = HTTPWrappers(client)

    def index(self):
        url = '/'
        name = 'index'
        headers = {'Accept': 'application/json'}
        response = self.client.get_request(url, name, headers)

        if 'index' in response.text:
            response.success()
        else:
            response.failure('Got wrong response')

    def route_a(self):
        url = '/a'
        name = 'route_a'
        headers = {'Accept': 'application/json'}
        response = self.client.get_request(url, name, headers)

        if 'route_a' in response.text:
            response.success()
        else:
            response.failure('Got wrong response')

    def route_b(self):
        url = '/b'
        name = 'route_b'
        headers = {'Accept': 'application/json'}
        response = self.client.get_request(url, name, headers)

        if 'route_b' in response.text:
            response.success()
        else:
            response.failure('Got wrong response')
