from datetime import datetime

from ..constants import DomainType
from ..ecosystem.constants import Ecosystem
from ..proposal import Proposal
from ..type-base import DomainEventBaseContext


class Registry:
    def __init__(
            self,
            id: str,
            name: str,
            host: str,
            ecosystem: Ecosystem,
            account_name: str | None,
            account_secret: str | None,
            created_at: datetime,
            updated_at: datetime
    ) -> None:
        self.id = id
        self.name = name
        self.host = host
        self.ecosystem = ecosystem
        self.account_name = account_name
        self.account_secret = account_secret
        self.created_at = created_at
        self.updated_at = updated_at


class RegistryEventContext(DomainEventBaseContext):
    def __init__(
            self,
            type: DomainType.REGISTRY,
            data: Registry
    ) -> None:
        self.type = type
        self.data = data
