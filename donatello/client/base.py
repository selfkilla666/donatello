
from __future__ import annotations

from abc import abstractmethod

from donatello.driver import APIDriver, AsyncAPIDriver
from donatello.models import *


class BaseDonatelloClient:

    __user_token__: str
    __api_driver__: APIDriver | AsyncAPIDriver
    is_polling: bool

    def __init__(self, token: str, driver: APIDriver | AsyncAPIDriver, *, is_polling: bool = False) -> None:
        self.__user_token__ = token
        self.__api_driver__ = driver
        self.is_polling = is_polling

    @property
    def __token_headers__(self) -> dict:
        return {"X-Token": self.__user_token__}

    @abstractmethod
    def get_me(self) -> User:
        """
        Інформація про користувача (себе)

        :return: User
        """
        ...

    @abstractmethod
    def get_donates(self, *, page: int = 0, size: int = 20) -> DonateList:
        """
        Отримати список останніх донатів

        :param page: Сторінка списку донатів, за замовчуванням 0
        :param size: Кількість донатів на одній сторінці
        :return: DonateList
        """
        ...

    @abstractmethod
    def get_clients(self) -> ClientList:
        """
        Отримати топ донатерів

        :return: ClientList
        """
        ...