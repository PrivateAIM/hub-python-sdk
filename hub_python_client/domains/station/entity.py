from datetime import datetime
from typing import Optional
from pydantic import BaseModel
from ..ecosystem import Ecosystem
from ..registry import Registry
from ..registry_project import RegistryProject
from ..types_base import DomainEventBaseContext
from ..constants import DomainType


class Station(BaseModel):
    id: str
    external_name: Optional[str] = None
    name: str
    public_key: Optional[str] = None
    email: Optional[str] = None
    ecosystem: Optional[Ecosystem] = None
    hidden: bool
    registry_id: str
    registry: Registry
    registry_project_id: Optional[str] = None
    registry_project: RegistryProject
    realm_id: str
    created_at: datetime
    updated_at: datetime


class StationEventContext(DomainEventBaseContext):
    type: DomainType.STATION
    data: Station
