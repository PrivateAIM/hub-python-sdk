from .entity import MasterImageGroup, MasterImageGroupManyResponse
from ..base import BaseAPI


class MasterImageGroupAPI(BaseAPI):
    async def get_many(self) -> MasterImageGroupManyResponse:
        response = await self.client.get(f'/api/master-image-groups')
        response_json = await response.json()
        return response_json

    async def get_one(self, id: str) -> MasterImageGroup:
        response = await self.client.get(f'/api/master-image-groups/{id}')
        response_json = await response.json()
        return response_json
