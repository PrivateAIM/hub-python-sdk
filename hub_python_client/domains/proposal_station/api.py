from .entity import ProposalStation
from ..base import BaseAPI

class ProposalStationAPI(BaseAPI):
    async def get_many(self) -> dict:
        response = await self.client.get('/api/proposal-stations')
        response_json = await response.json()
        return response_json

    async def get_one(self,id: str) -> ProposalStation:
        response = await self.client.get(f'/api/proposal-stations/{id}')
        response_json = await response.json()
        return response_json

    async def create(self, data: ProposalStation) -> ProposalStation:
        response = await self.client.post('/api/proposal-stations', json=data)
        response_json = await response.json()
        return response_json

    async def update(self, id: str, data: ProposalStation) -> ProposalStation:
        response = await self.client.post(f'/api/proposal-stations/{id}', json=data)
        response_json = await response.json()
        return response_json

    async def delete(self, id: str) -> ProposalStation:
        response = await self.client.delete(f'/api/proposal-stations/{id}')
        response_json = await response.json()
        return response_json
