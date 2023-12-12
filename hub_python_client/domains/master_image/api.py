from ..base import BaseAPI
from .entity import MasterImage
from .constants import MasterImageCommand
from typing import Optional, Dict, Any

class MasterImageAPI(BaseAPI):
    async def get_many(self):
        response = await self.client.get('/api/master-images')
        response_json = await response.json()
        return response_json

    async def get_one(self, id: str):
        response = await self.client.get(f'/api/master-images/{id}')
        response_json = await response.json()
        return response_json

    async def delete(self, id: str):
        response = await self.client.delete(f'/api/master-images/{id}')
        response_json = await response.json()
        return response_json

    async def run_command(self, command: MasterImageCommand):
        action_data = {'command': command}
        response = await self.client.post('/api/master-images/command', data=action_data)
        response_json = await response.json()
        return response_json
