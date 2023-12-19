from enum import Enum

class ProposalStationApprovalCommand(Enum):
    APPROVE = 'approve'
    REJECT = 'reject'

class ProposalStationApprovalStatus(Enum):
    REJECTED = 'rejected'
    APPROVED = 'approved'

class ProposalStationSocketServerToClientEventName(Enum):
    CREATED = 'proposalStationCreated'
    UPDATED = 'proposalStationUpdated'
    DELETED = 'proposalStationDeleted'

class ProposalStationSocketClientToServerEventName(Enum):
    SUBSCRIBE = 'proposalStationSubscribe'
    UNSUBSCRIBE = 'proposalStationUnsubscribe'
    IN_SUBSCRIBE = 'proposalStationInSubscribe'
    IN_UNSUBSCRIBE = 'proposalStationInUnsubscribe'
    OUT_SUBSCRIBE = 'proposalStationOutSubscribe'
    OUT_UNSUBSCRIBE = 'proposalStationOutUnsubscribe'
