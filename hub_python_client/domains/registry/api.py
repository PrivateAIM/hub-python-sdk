from typing import Any, Optional
import asyncio

from ..base import BaseAPI
from .entity import Registry
from ..utils import nullify_empty_object_properties


class RegistryAPI(BaseAPI):
    async def getMany(self):
        response = await self.client.get(f'registries')
        return response.data

    async def getOne(self,id: str):
        response = await self.client.get(f'registries/{id}')
        return response.data

    async def create(self,data: dict[str, Any]):
        response = await self.client.post('registries', nullify_empty_object_properties(data))
        return response.data

    async def update(self,id: str,data: dict[str, Any]):
        response = await self.client.post(f'registries/{id}', nullify_empty_object_properties(data))
        return response.data

    async def delete(self,id: str):
        response = await self.client.delete(f'registries/{id}')
        return response.data
