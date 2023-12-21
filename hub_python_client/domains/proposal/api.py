from ..base import BaseAPI
from .entity import Proposal, ProposalCreate, ProposalManyResponse


class ProposalAPI(BaseAPI):
    async def get_many(self) -> ProposalManyResponse:
        response = await self.client.get("/api/proposals")
        response_json = await response.json()
        return response_json

    async def get_one(self, id: str) -> Proposal:
        response = await self.client.get(f"/api/proposals/{id}")
        response_json = await response.json()
        return response_json

    async def create(self, data: ProposalCreate) -> Proposal:
        response = await self.client.post("/api/proposals", json=data)
        response_json = await response.json()
        return response_json

    async def update(self, id: str, data: ProposalCreate) -> Proposal:
        response = await self.client.post(f"/api/proposals/{id}", json=data)
        response_json = await response.json()
        return response_json

    async def delete(self, id: str) -> Proposal:
        response = await self.client.delete(f"/api/proposals/{id}")
        response_json = await response.json()
        return response_json
