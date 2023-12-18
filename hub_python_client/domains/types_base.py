from typing import TypeVar, Generic, List, Dict, Any, Optional, Union
from pydantic import BaseModel
from .constants import DomainEventName

R = TypeVar('R')


class SingleResourceResponse(Generic[R]):
    data: R


class CollectionResourceResponse(Generic[R]):
    data: List[R]
    meta: Dict[str, int]


class DomainEntityWithID(BaseModel):
    id: Any
    # Add other fields as needed


T = TypeVar('T', bound=DomainEntityWithID)


class DomainAPISlim(Generic[T]):
    def get_many(self, record: Optional[Dict[str, Any]] = None) -> CollectionResourceResponse[T]:
        pass

    def get_one(self, id: Any, record: Optional[Dict[str, Any]] = None) -> SingleResourceResponse[T]:
        pass

    def delete(self, id: Any) -> SingleResourceResponse[T]:
        pass

    def create(self, data: Dict[str, Any]) -> SingleResourceResponse[T]:
        pass


class DomainAPI(DomainAPISlim[T]):
    def update(self, id: Any, data: Dict[str, Any]) -> SingleResourceResponse[T]:
        pass


class BaseAPIContext(BaseModel):
    client: Optional[
        Union['Client', 'RequestBaseOptions']]  # Replace 'Client' and 'RequestBaseOptions' with actual types


class DomainEventBaseContext(BaseModel):
    event: DomainEventName
    type: str


class Meta(BaseModel):
    total: int
