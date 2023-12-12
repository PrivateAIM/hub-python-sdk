from enum import Enum

class DomainType(Enum):
    MASTER_IMAGE = 'masterImage'
    MASTER_IMAGE_GROUP = 'masterImageGroup'
    PROPOSAL = 'proposal'
    PROPOSAL_STATION = 'proposalStation'
    REGISTRY = 'registry'
    REGISTRY_PROJECT = 'registryProject'
    STATION = 'station'
    SERVICE = 'service'
    TRAIN = 'train'
    TRAIN_FILE = 'trainFile'
    TRAIN_LOG = 'trainLog'
    TRAIN_STATION = 'trainStation'
    USER_SECRET = 'userSecret'

class DomainSubType(Enum):
    PROPOSAL_STATION_IN = 'proposalStationIn'
    PROPOSAL_STATION_OUT = 'proposalStationOut'
    TRAIN_STATION_IN = 'trainStationIn'
    TRAIN_STATION_OUT = 'TrainStationOut'

class DomainEventName(Enum):
    CREATED = 'created'
    DELETED = 'deleted'
    UPDATED = 'updated'

class DomainEventSubscriptionName(Enum):
    SUBSCRIBE = 'subscribe'
    UNSUBSCRIBE = 'unsubscribe'