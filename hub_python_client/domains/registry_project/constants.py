from enum import Enum

class RegistryProjectType(Enum):
    DEFAULT = 'default'
    AGGREGATOR = 'aggregator'
    INCOMING = 'incoming'
    OUTGOING = 'outgoing'
    MASTER_IMAGES = 'masterImages'
    STATION = 'station'

class RegistryProjectSocketServerToClientEventName(Enum):
    CREATED = 'registryProjectCreated'
    UPDATED = 'registryProjectUpdated'
    DELETED = 'registryProjectDeleted'

class RegistryProjectSocketClientToServerEventName(Enum):
    SUBSCRIBE = 'registryProjectSubscribe'
    UNSUBSCRIBE = 'registryProjectUnsubscribe'