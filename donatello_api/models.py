
from __future__ import annotations
from typing import Optional, List, Sequence, Dict, Any
from datetime import datetime as Datetime
from pydantic import BaseModel, Field, validator


class UserDonates(BaseModel):

    total_amount: int = Field(alias="totalAmount")
    total_count: int = Field(alias="totalCount")

    def __repr__(self) -> Dict[str, Any]:
        return self.dict()

class User(BaseModel):

    nickname: str = Field(alias="nickname")
    id: str = Field(alias="pubId")
    page: str = Field(alias="page")
    is_active: bool = Field(alias="isActive")
    is_public: bool = Field(alias="isPublic")
    donates: UserDonates = Field(alias="donates")
    created_at: Datetime = Field(alias="createdAt")

    @validator("created_at", pre=True)
    def validate_created_at(cls, value) -> Datetime:
        return Datetime.strptime(value, "%Y-%m-%d %H:%M:%S")

    def __str__(self) -> str:
        return f"<User:{self.id}>"

    def __repr__(self) -> Dict[str, Any]:
        return self.dict()

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
        return f"<Donate:{self.id}>"

    def __repr__(self) -> Dict[str, Any]:
        return self.dict()

    def __lt__(self: Donate, other: Donate) -> bool:
        return self.amount < other.amount

class DonateList(BaseModel):

    content: Optional[List[Donate]] = Field(alias="content")
    page: Optional[int] = Field(alias="page")
    size: Optional[int] = Field(alias="size")
    num: Optional[int] = Field(alias="num", default=0)
    first: Optional[bool] = Field(alias="first")
    last: Optional[bool] = Field(alias="last")
    total: Optional[int] = Field(alias="total")

    def __iter__(self) -> Sequence[Donate]:
        for element in self.content:
            yield element

    def __getitem__(self, item: int) -> Donate:
        return self.content[item]

    def __repr__(self) -> Dict[str, Any]:
        return self.dict()

    def __len__(self) -> int:
        return len(self.content)

    def __str__(self) -> str:
        return f"<DonateList: {self.content}>"

class Client(BaseModel):

    client_name: Optional[str] = Field(alias="clientName")
    total_amount: Optional[int] = Field(alias="totalAmount")

    def __repr__(self) -> Dict[str, Any]:
        return self.dict()

    def __lt__(self: Client, other: Client) -> bool:
        return self.total_amount < other.total_amount

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