# https://github.com/selfkilla666/donatello
# Code by selfkilla666
# MIT License


from __future__ import annotations
from abc import abstractmethod
from typing import Any


class BaseAPIDriver:
    API_URL = "https://donatello.to/api"

    def __init__(self, version: str) -> None:
        self.version: str = version

    def __generate_action_url__(self, action: str) -> str:
        return f"{self.API_URL}/{self.version}/{action}"

    @abstractmethod
    def call_action(self, *args, **kwargs) -> NotImplementedError | Any:
        raise NotImplementedError
