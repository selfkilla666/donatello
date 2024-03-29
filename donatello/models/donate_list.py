# https://github.com/selfkilla666/donatello
# Code by selfkilla666
# MIT License


from __future__ import annotations
from typing import Dict, List, Sequence, Union
from pydantic import BaseModel, Field

from .donate import Donate


class DonateList(BaseModel):

    content: List[Donate] = Field(alias="content", default=[])
    page: int = Field(alias="page", default=0)
    size: int = Field(alias="size", default=20)
    num: int = Field(alias="num", default=0)
    first: bool = Field(alias="first")
    last: bool = Field(alias="last")
    total: int = Field(alias="total")

    def __iter__(self) -> Sequence[Donate]:
        for element in self.content:
            yield element

    def __getitem__(self, item: int) -> Donate:
        return self.content[item]

    def __repr__(self) -> Dict[str, Union[int, bool, List[Donate]]]:
        return self.dict()

    def __len__(self) -> int:
        return len(self.content)

    def __str__(self) -> str:
        return f"{self.dict()}"