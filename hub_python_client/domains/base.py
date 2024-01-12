# import aiohttp
import asyncio
import httpx


class BaseAPI:
    def __init__(self, username=None, password=None, base_url=None):
        self.username = username
        self.password = password
        self.base_url = base_url
        self.client = httpx.AsyncClient(base_url=self.base_url, auth=httpx.BasicAuth(self.username, self.password))
