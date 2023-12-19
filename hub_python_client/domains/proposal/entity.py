from typing import Optional, List
from pydantic import BaseModel
from datetime import datetime
from ..constants import DomainType
from ..types_base import DomainEventBaseContext, Meta
from ..master_image import MasterImage
from .constants import ProposalRisk


class Proposal(BaseModel):
    id: str
    title: str
    requested_data: str
    risk: ProposalRisk
    risk_comment: str
    trains: int
    created_at: datetime
    updated_at: datetime
    realm_id: str
    user_id: str

    master_image_id: Optional[str]
    master_image: Optional[MasterImage]


class ProposalEventContext(DomainEventBaseContext):
    type: str = f"{DomainType.PROPOSAL}"
    data: Proposal


class ProposalManyResponse(BaseModel):
    data: List[Proposal]
    meta: Meta
