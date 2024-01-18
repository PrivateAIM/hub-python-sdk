from typing import Dict, Any
from ..base import BaseAPI
from .entity import Station , StationCreate
from ..types_base import CollectionResourceResponse, SingleResourceResponse
from ..utils import nullify_empty_object_properties


class StationAPI(BaseAPI):

    async def get_many(self) -> CollectionResourceResponse[Station]:
        response = await self.client.get("/api/stations")
        response.raise_for_status()
        response_json = response.json()
        return response_json

    async def get_one(self, id: str) -> SingleResourceResponse[Station]:
        response = await self.client.get(f"/api/stations/{id}")
        response.raise_for_status()
        response_json = response.json()
        return response_json

    async def create(self, data: StationCreate) -> SingleResourceResponse[Station]:
        response = await self.client.post("/api/stations", json=nullify_empty_object_properties(data))
        response.raise_for_status()
        response_json = response.json()
        return response_json

    async def update(self, id: str, data: Dict[str, Any]) -> SingleResourceResponse[Station]:
        response = await self.client.post(f"/api/stations/{id}", json=nullify_empty_object_properties(data))
        response.raise_for_status()
        response_json = response.json()
        return response_json

    async def delete(self, id: str) -> SingleResourceResponse[Station]:
        response = await self.client.delete(f"/api/stations/{id}")
        response.raise_for_status()
        response_json = response.json()
        return response_json

    async def run_command(self, id: str, task: str, data: Dict[str, Any]) -> SingleResourceResponse[Station]:
        response = await self.client.post(f"/api/stations/{id}/task", json={"task": task, **data})
        response.raise_for_status()
        response_json = response.json()
        return response_json
