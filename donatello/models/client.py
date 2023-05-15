# https://github.com/selfkilla666/donatello
# Code by selfkilla666
# MIT License


from __future__ import annotations
from typing import Dict, Union
from pydantic import BaseModel, Field


class Client(BaseModel):

    client_name: str = Field(alias="clientName")
    total_amount: int = Field(alias="totalAmount")

    def __repr__(self) -> Dict[str, Union[str, int]]:
        return self.dict()

    def __str__(self) -> str:
        return f"{self.dict()}"

    def __lt__(self: Client, other: Client) -> bool:
        return self.total_amount < other.total_amount