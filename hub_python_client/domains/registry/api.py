from typing import Any, Optional

from rapiq import BuildInput, buildQuery
from hub-python-client.domains.base import BaseAPI
from .entity import Registry
from hub-python-client.domains.types-base import CollectionResourceResponse, SingleResourceResponse
from hub-python-client.utils import nullifyEmptyObjectProperties


class RegistryAPI(BaseAPI):
    async def getMany(
            self,
            options: Optional[BuildInput[Registry]]
    ) -> await CollectionResourceResponse[Registry]:
        response = await self.client.get(f'registries/{buildQuery(options)}')
        return response.data

    async def getOne(
            self,
            id: str,
            options: Optional[BuildInput[Registry]]
    ) -> await SingleResourceResponse[Registry]:
        response = await self.client.get(f'registries/{id}{buildQuery(options)}')
        return response.data

    async def create(
            self,
            data: dict[str, Any]
    ) -> await SingleResourceResponse[Registry]:
        response = await self.client.post('registries', nullifyEmptyObjectProperties(data))
        return response.data

    async def update(
            self,
            id: str,
            data: dict[str, Any]
    ) -> await SingleResourceResponse[Registry]:
        response = await self.client.post(f'registries/{id}', nullifyEmptyObjectProperties(data))
        return response.data

    async def delete(
            self,
            id: str
    ) -> await SingleResourceResponse[Registry]:
        response = await self.client.delete(f'registries/{id}')
        return response.data
