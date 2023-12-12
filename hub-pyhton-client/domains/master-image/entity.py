from datetime import datetime
from typing import Optional
from pydantic import BaseModel
from ..constants import DomainType
from ..types_base import DomainEventBaseContext

class MasterImage(BaseModel):
    id: str
    path: Optional[str]
    virtual_path: str
    group_virtual_path: str
    name: str
    command: Optional[str]
    command_arguments: Optional[dict]
    created_at: datetime
    updated_at: datetime

class MasterImageEventContext(DomainEventBaseContext):
    type: str = f"{DomainType.MASTER_IMAGE}"
    data: MasterImage