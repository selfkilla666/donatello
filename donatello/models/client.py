
from __future__ import annotations
from typing import Dict, Any, Optional
from pydantic import BaseModel, Field


class Client(BaseModel):

    client_name: Optional[str] = Field(alias="clientName")
    total_amount: Optional[int] = Field(alias="totalAmount")

    def __repr__(self) -> Dict[str, Any]:
        return self.dict()

    def __str__(self) -> str:
        return f"{self.dict()}"

    def __lt__(self: Client, other: Client) -> bool:
        return self.total_amount < other.total_amount