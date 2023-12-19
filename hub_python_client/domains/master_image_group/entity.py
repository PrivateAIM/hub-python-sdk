from datetime import datetime
from typing import Optional, Any, List
from pydantic import BaseModel
from ..constants import DomainType
from ..types_base import DomainEventBaseContext, Meta


class MasterImageGroup(BaseModel):
    id: str
    name: str
    path: str
    virtual_path: str
    command: Optional[str]
    command_arguments: Optional[Any]
    created_at: datetime
    updated_at: datetime


class MasterImageGroupEventContext(DomainEventBaseContext):
    type: str = f"{DomainType.MASTER_IMAGE_GROUP}"
    data: MasterImageGroup


class MasterImageGroupManyResponse(BaseModel):
    data: List[MasterImageGroup]
    meta: Meta
