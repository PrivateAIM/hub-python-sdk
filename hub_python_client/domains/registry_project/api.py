from .entity import RegistryProject, RegistryProjectManyResponse
from ..base import BaseAPI

class RegistryProjectAPI(BaseAPI):
    async def get_many(self) -> RegistryProjectManyResponse:
        response = await self.client.get('/api/registry-projects')
        response_json = await response.json()
        return response_json

    async def get_one(self,id: str) -> RegistryProject:
        response = await self.client.get(f'/api/registry-projects/{id}')
        response_json = await response.json()
        return response_json

    async def create(self, data: RegistryProject) -> RegistryProject:
        response = await self.client.post('/api/registry-projects', json=data)
        response_json = await response.json()
        return response_json

    async def update(self, id: str, data: RegistryProject) -> RegistryProject:
        response = await self.client.post(f'/api/registry-projects/{id}', json=data)
        response_json = await response.json()
        return response_json

    async def delete(self, id: str) -> RegistryProject:
        response = await self.client.delete(f'/api/registry-projects/{id}')
        response_json = await response.json()
        return response_json
