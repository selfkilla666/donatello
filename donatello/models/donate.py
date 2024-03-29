# https://github.com/selfkilla666/donatello
# Code by selfkilla666
# MIT License


from __future__ import annotations
from typing import Dict, Union
from datetime import datetime as Datetime
from pydantic import BaseModel, Field, validator


class Donate(BaseModel):
    id: str = Field(alias="pubId")
    client_name: str = Field(alias="clientName")
    message: str = Field(alias="message")
    amount: int = Field(alias="amount")
    currency: str = Field(alias="currency")
    goal: str = Field(alias="goal", default="")
    is_published: bool = Field(alias="isPublished")
    created_at: Datetime = Field(alias="createdAt")

    @validator("created_at", pre=True)
    def validate_created_at(cls, value) -> Datetime:
        return Datetime.strptime(value, "%Y-%m-%d %H:%M:%S")

    def __str__(self) -> str:
        return f"{self.dict()}"

    def __repr__(self) -> Dict[str, Union[str, int, bool, Datetime]]:
        return self.dict()

    def __lt__(self: Donate, other: Donate) -> bool:
        return self.amount < other.amount
