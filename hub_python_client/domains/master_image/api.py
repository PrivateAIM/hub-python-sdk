from ..base import BaseAPI
from .entity import MasterImage ,MasterImageManyResponse
from .constants import MasterImageCommand


class MasterImageAPI(BaseAPI):
    async def get_many(self) -> MasterImageManyResponse:
        response = await self.client.get('/api/master-images')
        response_json = response.json()
        return response_json

    async def get_one(self, id: str) -> MasterImage:
        response = await self.client.get(f'/api/master-images/{id}')
        response_json = response.json()
        return response_json

    async def delete(self, id: str):
        response = await self.client.delete(f'/api/master-images/{id}')
        response_json = response.json()
        return response_json

    async def run_command(self, command: MasterImageCommand):
        action_data = {'command': command}
        response = await self.client.post('/api/master-images/command', data=action_data)
        response_json = response.json()
        return response_json
