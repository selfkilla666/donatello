from __future__ import annotations

from requests import Response

from donatello.driver import APIDriver
from donatello.client import BaseDonatelloClient
from donatello.exceptions import *
from donatello.models import *


CURRENT_API_VERSION = "v1"


class DonatelloClient(BaseDonatelloClient):
    """ Клас клієнта для роботи з API Donatello """

    def __init__(self, token: str, *, is_polling: bool = False, version: str = CURRENT_API_VERSION) -> None:
        super().__init__(token, APIDriver(version), is_polling=is_polling)

    def get_me(self) -> User:

        response: Response = self.__api_driver__.call_action(
            "me",
            self.__token_headers__,
            method="get"
        )

        if response.status_code == 401:
            raise AuthenticateError(response.json().get("message"))
        elif response.status_code == 404:
            raise IncompleteProfileSettings(response.json().get("message"))

        return User.parse_obj(response.json())

    def get_donates(self, *, page: int = 0, size: int = 20) -> DonateList:

        response: Response = self.__api_driver__.call_action(
            "donates",
            self.__token_headers__,
            params={"page": page, "size": size},
            method="get"
        )

        if response.status_code == 401:
            raise AuthenticateError(response.json().get("message"))

        return DonateList.parse_obj(response.json())

    def get_clients(self) -> ClientList:

        response: Response = self.__api_driver__.call_action(
            "clients",
            self.__token_headers__,
            method="get"
        )

        if response.status_code == 401:
            raise AuthenticateError(response.json().get("message"))

        return ClientList.parse_obj(response.json())
