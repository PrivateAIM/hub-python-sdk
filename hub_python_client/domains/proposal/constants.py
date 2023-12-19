from enum import Enum


class ProposalRisk(Enum):
    LOW = 'low'
    MID = 'mid'
    HIGH = 'high'


class ProposalSocketServerToClientEventName(Enum):
    CREATED = 'proposalCreated'
    UPDATED = 'proposalUpdated'
    DELETED = 'proposalDeleted'


class ProposalSocketClientToServerEventName(Enum):
    SUBSCRIBE = 'proposalSubscribe'
    UNSUBSCRIBE = 'proposalUnsubscribe'
