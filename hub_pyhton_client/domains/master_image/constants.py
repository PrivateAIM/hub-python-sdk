from enum import Enum

class MasterImageCommand(Enum):
    SYNC = 'sync'

class MasterImageGroupType(Enum):
    LANGUAGE = 'language'
    DEFAULT = 'default'