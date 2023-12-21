from datetime import datetime
from typing import List, Optional

from pydantic import BaseModel

from ..constants import DomainType
from ..proposal import Proposal
from ..station import Station
from ..types_base import DomainEventBaseContext, Meta
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


class ProposalStationCreate(BaseModel):
    approval_status: Optional[ProposalStationApprovalStatus]
    comment: Optional[str]
    proposal_id: str
    station_id: str


class ProposalStationUpdate(BaseModel):
    approval_status: Optional[ProposalStationApprovalStatus]
    comment: Optional[str]


class ProposalStationEventContext(DomainEventBaseContext):
    type: str = f"{DomainType.PROPOSAL_STATION}"
    data: ProposalStation


class ProposalStationManyResponse(BaseModel):
    data: List[ProposalStation]
    meta: Meta
