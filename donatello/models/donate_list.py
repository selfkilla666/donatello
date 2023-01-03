
from __future__ import annotations
from typing import Dict, List, Sequence, Any, Optional
from pydantic import BaseModel, Field

from donatello.models import Donate


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