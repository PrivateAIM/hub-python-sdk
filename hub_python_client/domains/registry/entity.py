from datetime import datetime
from typing import Optional
from ..ecosystem import Ecosystem
from ..types_base import DomainEventBaseContext
from pydantic import BaseModel


class Registry(BaseModel):
    id: str
    name: str
    host: str
    ecosystem: Ecosystem
    account_name: Optional[str] = None
    account_secret: Optional[str] = None
    created_at: datetime
    updated_at: datetime

class RegistryEventContext(DomainEventBaseContext):
    type: str
    data: Registry