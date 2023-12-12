import aiohttp

class BaseAPI:
    def __init__(self, client=None):
        self.client = client

    def set_client(self, client):
        if isinstance(client, aiohttp.ClientSession):
            self.client = client
        else:
            self.client = aiohttp.ClientSession()

api = BaseAPI()
