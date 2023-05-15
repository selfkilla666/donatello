# https://github.com/selfkilla666/donatello
# Code by selfkilla666
# MIT License


from __future__ import annotations
from typing import Dict
from pydantic import BaseModel, Field


class UserDonates(BaseModel):

    total_amount: int = Field(alias="totalAmount")
    total_count: int = Field(alias="totalCount")

    def __repr__(self) -> Dict[str, int]:
        return self.dict()

    def __str__(self) -> str:
        return f"{self.dict()}"

    def __lt__(self, other: UserDonates) -> bool:
        return self.total_amount < other.total_amount