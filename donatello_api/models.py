
from typing import List, Iterator
from datetime import datetime
from pydantic import BaseModel, Field, validator


class UserDonates(BaseModel):
    total_amount: int = Field(alias="totalAmount")
    total_count: int = Field(alias="totalCount")

class User(BaseModel):
    nickname: str = Field(alias="nickname")
    id: str = Field(alias="pubId")
    page: str = Field(alias="page")
    is_active: bool = Field(alias="isActive")
    is_public: bool = Field(alias="isPublic")
    donates: UserDonates = Field(alias="donates")
    created_at: datetime = Field(alias="createdAt")

    @validator("created_at", pre=True)
    def validate_created_at(cls, value) -> datetime:
        return datetime.strptime(value, "%Y-%m-%d %H:%M:%S")

    def __str__(self) -> str:
        return f"<User:{self.id}>"

class Donate(BaseModel):
    id: str = Field(alias="pubId")
    client_name: str = Field(alias="clientName")
    message: str = Field(alias="message")
    amount: int = Field(alias="amount")
    currency: str = Field(alias="currency")
    goal: str = Field(alias="goal", default="")
    is_published: bool = Field("isPublished")
    created_at: datetime = Field(alias="createdAt")

    @validator("created_at", pre=True)
    def validate_created_at(cls, value) -> datetime:
        return datetime.strptime(value, "%Y-%m-%d %H:%M:%S")

    def __str__(self) -> str:
        return f"<Donate:{self.id}>"

class DonateList(BaseModel):
    content: List[Donate] = Field(alias="content")
    page: int = Field(alias="page")
    size: int = Field(alias="size")
    num: int = Field(alias="num", default=0)
    first: bool = Field(alias="first")
    last: bool = Field(alias="last")
    total: int = Field(alias="total")

    def __iter__(self) -> Iterator[Donate]:
        for element in self.content:
            yield element

    def __len__(self) -> int:
        return len(self.content)

    def __str__(self) -> str:
        return f"<DonateList: {self.content}>"

class Client(BaseModel):
    client_name: str = Field(alias="clientName")
    total_amount: int = Field(alias="totalAmount")

class ClientList(BaseModel):
    clients = List[Client] = Field(alias="clients")

    def __iter__(self) -> Iterator[Client]:
        for element in self.clients:
            yield element

    def __len__(self) -> int:
        return len(self.clients)

    def __str__(self) -> str:
        return f"<ClientList: {self.clients}>"