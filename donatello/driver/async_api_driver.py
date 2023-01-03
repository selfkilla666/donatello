
from __future__ import annotations
from aiohttp import ClientSession, ClientResponse

from donatello.driver import BaseAPIDriver


class AsyncAPIDriver(BaseAPIDriver):
    def __init__(self, version: str) -> None:
        super().__init__(version)

    async def call_action(self, action: str, headers: dict, *, params: dict = {}, method: str = "get") -> ClientResponse:
        async with ClientSession() as session:
            async with session.request(
                    method=method,
                    url=self.__generate_action_url__(action),
                    headers=headers,
                    params=params
            ) as response:
                return response
