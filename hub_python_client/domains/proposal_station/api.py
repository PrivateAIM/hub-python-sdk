from ..base import BaseAPI
from .entity import ProposalStation, ProposalStationCreate, ProposalStationUpdate


class ProposalStationAPI(BaseAPI):
    async def get_many(self) -> dict:
        response = await self.client.get("/api/proposal-stations")
        response.raise_for_status()
        response_json = response.json()
        return response_json

    async def get_one(self, id: str) -> ProposalStation:
        response = await self.client.get(f"/api/proposal-stations/{id}")
        response.raise_for_status()
        response_json = response.json()
        return response_json

    async def create(self, data: ProposalStationCreate) -> ProposalStation:
        response = await self.client.post("/api/proposal-stations", json=data)
        response.raise_for_status()
        response_json = response.json()
        return response_json

    async def update(self, id: str, data: ProposalStationUpdate) -> ProposalStation:
        response = await self.client.post(f"/api/proposal-stations/{id}", json=data)
        response.raise_for_status()
        response_json = response.json()
        return response_json

    async def delete(self, id: str) -> ProposalStation:
        response = await self.client.delete(f"/api/proposal-stations/{id}")
        response.raise_for_status()
        response_json = response.json()
        return response_json
