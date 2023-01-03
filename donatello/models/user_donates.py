
from __future__ import annotations
from typing import Dict, Any
from pydantic import BaseModel, Field


class UserDonates(BaseModel):

    total_amount: int = Field(alias="totalAmount")
    total_count: int = Field(alias="totalCount")

    def __repr__(self) -> Dict[str, Any]:
        return self.dict()

    def __str__(self) -> str:
        return f"{self.dict()}"