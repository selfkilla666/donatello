
from __future__ import annotations
from typing import Dict, Any, Optional
from datetime import datetime as Datetime
from pydantic import BaseModel, Field, validator


class Donate(BaseModel):

    id: Optional[str] = Field(alias="pubId")
    client_name: Optional[str] = Field(alias="clientName")
    message: Optional[str] = Field(alias="message")
    amount: Optional[int] = Field(alias="amount")
    currency: Optional[str] = Field(alias="currency")
    goal: Optional[str] = Field(alias="goal", default="")
    is_published: Optional[bool] = Field(alias="isPublished")
    created_at: Optional[Datetime] = Field(alias="createdAt")

    @validator("created_at", pre=True)
    def validate_created_at(cls, value) -> Datetime:
        return Datetime.strptime(value, "%Y-%m-%d %H:%M:%S")

    def __str__(self) -> str:
        return f"{self.dict()}"

    def __repr__(self) -> Dict[str, Any]:
        return self.dict()

    def __lt__(self: Donate, other: Donate) -> bool:
        return self.amount < other.amount