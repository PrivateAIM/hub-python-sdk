from typing import Optional , List
from pydantic import BaseModel
from datetime import datetime
from ..constants import DomainType
from ..types_base import DomainEventBaseContext, Meta
from ..proposal import Proposal
from ..station import Station
from .constants import ProposalStationApprovalStatus

class ProposalStation(BaseModel):
    id: str
    approval_status: Optional[ProposalStationApprovalStatus]
    comment: Optional[str]
    created_at: datetime
    updated_at: datetime
    proposal_id: str
    proposal: Proposal
    proposal_realm_id: str
    station_id: str
    station: Station
    station_realm_id: str

class ProposalStationEventContext(DomainEventBaseContext):
    type: str = f"{DomainType.PROPOSAL_STATION}"
    data: ProposalStation

class ProposalStationManyResponse(BaseModel):
    data: List[ProposalStation]
    meta: Meta
