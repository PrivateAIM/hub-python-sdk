# import aiohttp
import asyncio
import httpx


class BaseAPI:
    def __init__(self, username=None, password=None, base_url=None):
        self.username = username
        self.password = password
        self.base_url = base_url
        self.client = None
        loop = asyncio.get_event_loop()
        loop.run_until_complete(self.set_client(self.client))

    async def set_client(self, client):
        if isinstance(client, httpx.AsyncClient):
            self.client = client
        else:
            self.client = httpx.AsyncClient(base_url=self.base_url,
                                            auth = httpx.BasicAuth(self.username, self.password))

    async def close(self):
        # Assuming `self.client` is an instance of `ClientSession`
        await self.client.close()
