import aiohttp
import asyncio


class BaseAPI:
    def __init__(self, username=None, password=None, base_url=None):
        self.username = username
        self.password = password
        self.base_url = base_url
        self.client = None
        loop = asyncio.get_event_loop()
        loop.run_until_complete(self.set_client(self.client))

    async def set_client(self, client):
        if isinstance(client, aiohttp.ClientSession):
            self.client = client
        else:
            self.client = aiohttp.ClientSession(base_url=self.base_url,
                                                auth=aiohttp.BasicAuth(self.username,
                                                                       self.password))

    async def close(self):
        # Assuming `self.client` is an instance of `ClientSession`
        await self.client.close()
