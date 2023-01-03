from __future__ import annotations

from aiohttp import ClientResponse

from donatello.driver import AsyncAPIDriver
from donatello.client import BaseDonatelloClient
from donatello.exceptions import *
from donatello.models import *


CURRENT_API_VERSION = "v1"


class AsyncDonatelloClient(BaseDonatelloClient):

    def __init__(self, token: str, *, is_polling: bool = False, version: str = CURRENT_API_VERSION) -> None:
        super().__init__(token, AsyncAPIDriver(version), is_polling=is_polling)

    async def get_me(self) -> User:

        response: ClientResponse = await self.__api_driver__.call_action(
            "me",
            self.__token_headers__,
            method="get"
        )

        response_json = await response.json()

        if response.status == 401:
            raise AuthenticateError(response_json.get("message"))
        elif response.status == 404:
            raise IncompleteProfileSettings(response_json.get("message"))

        return User.parse_obj(response_json)

    async def get_donates(self, *, page: int = 0, size: int = 20) -> DonateList:

        response: ClientResponse = await self.__api_driver__.call_action(
            "donates",
            self.__token_headers__,
            params={"page": page, "size": size},
            method="get"
        )

        response_json = await response.json()

        if response.status == 401:
            raise AuthenticateError(response_json.get("message"))

        return DonateList.parse_obj(response_json)

    async def get_clients(self) -> ClientList:

        response: ClientResponse = await self.__api_driver__.call_action(
            "clients",
            self.__token_headers__,
            method="get"
        )

        response_json = await response.json()

        if response.status == 401:
            raise AuthenticateError(response_json.get("message"))

        return ClientList.parse_obj(response_json)
