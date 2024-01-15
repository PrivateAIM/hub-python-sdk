from ..base import BaseAPI
from .entity import Registry, RegistryManyResponse
from ..utils import nullify_empty_object_properties


class RegistryAPI(BaseAPI):
    async def getMany(self)-> RegistryManyResponse:
        response = await self.client.get('/api/registries')
        return response.json()

    async def getOne(self, id: str)-> Registry:
        response = await self.client.get(f'/api/registries/{id}')
        return response.json()

    async def create(self, data: Registry)-> Registry:
        response = await self.client.post('/api/registries', nullify_empty_object_properties(data))
        return response.json()

    async def update(self, id: str, data: Registry) -> Registry:
        response = await self.client.post(f'/api/registries/{id}', nullify_empty_object_properties(data))
        return response.json()

    async def delete(self, id: str)-> Registry:
        response = await self.client.delete(f'/api/registries/{id}')
        return response.json()
