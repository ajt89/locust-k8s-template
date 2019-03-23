class HTTPWrappers():

    def __init__(self, client):
        self.client = client

    def get_request(self, url, name, headers):
        return self.client.get(url, name=name, headers=headers, catch_response=True)
