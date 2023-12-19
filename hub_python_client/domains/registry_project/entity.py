from typing import Optional, List
from datetime import datetime
from .constants import RegistryProjectType
from ..constants import DomainType
from ..registry import Registry
from ..ecosystem import Ecosystem
from ..types_base import DomainEventBaseContext, Meta
from pydantic import BaseModel


class RegistryProject(BaseModel):
    id: str
    name: str
    ecosystem: Ecosystem
    type: RegistryProjectType
    public: bool
    external_name: str
    external_id: Optional[str]
    account_id: Optional[str]
    account_name: Optional[str]
    account_secret: Optional[str]
    webhook_name: Optional[str]
    webhook_exists: Optional[bool]
    registry_id: str
    registry: Registry
    realm_id: Optional[str]
    created_at: datetime
    updated_at: datetime


class RegistryProjectEventContext(DomainEventBaseContext):
    type: DomainType.REGISTRY_PROJECT
    data: RegistryProject


class RegistryProjectManyResponse(BaseModel):
    data: List[RegistryProject]
    meta: Meta
