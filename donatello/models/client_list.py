
from __future__ import annotations
from typing import Optional, List, Sequence, Dict, Any
from pydantic import BaseModel, Field

from donatello.models import Client


class ClientList(BaseModel):

    clients: Optional[List[Client]] = Field(alias="clients", default=[])

    def __iter__(self) -> Sequence[Client]:
        for element in self.clients:
            yield element

    def __getitem__(self, item: int) -> Client:
        return self.clients[item]

    def __repr__(self) -> Dict[str, Any]:
        return self.dict()

    def __len__(self) -> int:
        return len(self.clients)

    def __str__(self) -> str:
        return f"<ClientList: {self.clients}>"