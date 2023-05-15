# https://github.com/selfkilla666/donatello
# Code by selfkilla666
# MIT License


from __future__ import annotations
from typing import List, Sequence, Dict
from pydantic import BaseModel, Field

from donatello.models import Client


class ClientList(BaseModel):

    clients: List[Client] = Field(alias="clients", default=[])

    def __iter__(self) -> Sequence[Client]:
        for element in self.clients:
            yield element

    def __getitem__(self, item: int) -> Client:
        return self.clients[item]

    def __repr__(self) -> Dict[str, List[Client]]:
        return self.dict()

    def __len__(self) -> int:
        return len(self.clients)

    def __str__(self) -> str:
        return f"{self.dict()}"
