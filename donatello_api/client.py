
from typing import NoReturn

from donatello.driver import APIDriver
from donatello.exceptions import *
from donatello.models import *


class Donatello:

    def __init__(self, token: str, *, version: str = "v1") -> NoReturn:
        self.__user_token__ = token
        self.__api_driver__ = APIDriver(version=version)

    @property
    def __token_headers__(self) -> dict:
        return {"X-Token": self.__user_token__}

    def get_me(self) -> User:
        """
        Інформація про користувача (себе)

        :return: User
        """

        response = self.__api_driver__.call_action(
            "me",
            self.__token_headers__,
            method="get"
        )

        if response.status_code == 401:
            raise AuthenticateError(response.json()["message"])
        elif response.status_code == 404:
            raise IncompleteProfileSettings(response.json()["message"])

        return User.parse_raw(response.content)

    def get_donates(self, *, page: int = 0, size: int = 20) -> DonateList:
        """
        Отримати список останніх донатів

        :param page: Сторінка списку донатів, за замовчуванням 0
        :param size: Кількість донатів на одній сторінці
        :return: DonateList
        """

        response = self.__api_driver__.call_action(
            "donates",
            self.__token_headers__,
            params={"page": page, "size": size},
            method="get"
        )

        if response.status_code == 401:
            raise AuthenticateError(response.json()["message"])

        return DonateList.parse_raw(response.content)

    def get_clients(self) -> ClientList:
        """
        Отримати топ донатерів

        :return: ClientList
        """

        response = self.__api_driver__.call_action(
            "clients",
            self.__token_headers__,
            method="get"
        )

        if response.status_code == 401:
            raise AuthenticateError(response.json()["message"])

        return ClientList.parse_raw(response.content)