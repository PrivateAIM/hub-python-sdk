from typing import Dict, Any
from ..base import BaseAPI
from .entity import Station
from ..types_base import CollectionResourceResponse, SingleResourceResponse
from ..utils import nullify_empty_object_properties


class StationAPI(BaseAPI):
    async def get_many(self) -> CollectionResourceResponse[Station]:

        response = await self.client.get("/stations")
        response_json = response.json()
        return response_json

    async def get_one(self, id: str) -> SingleResourceResponse[Station]:
        response = await self.client.get(f"/stations/{id}")
        response_json = response.json()
        return response_json

    async def create(self, data: Dict[str, Any]) -> SingleResourceResponse[Station]:
        response = await self.client.post("/stations", json=nullify_empty_object_properties(data))
        response_json = response.json()
        return response_json

    async def update(self, id: str, data: Dict[str, Any]) -> SingleResourceResponse[Station]:
        response = await self.client.post(f"/stations/{id}", json=nullify_empty_object_properties(data))
        response_json = response.json()
        return response_json

    async def delete(self, id: str) -> SingleResourceResponse[Station]:
        response = await self.client.delete(f"/stations/{id}")
        response_json = response.json()
        return response_json

    async def run_command(self, id: str, task: str, data: Dict[str, Any]) -> SingleResourceResponse[Station]:
        response = await self.client.post(f"/stations/{id}/task", json={"task": task, **data})
        response_json = response.json()
        return response_json
