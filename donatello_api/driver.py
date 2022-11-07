
from typing import NoReturn
import requests


class BaseAPIDriver:

    API_URL = "https://donatello.to/api"

    def __init__(self, version: str) -> NoReturn:
        self.version = version

    def __generate_action_url__(self, action: str) -> str:
        return f"{self.API_URL}/{self.version}/{action}"

    def call_action(self, *args, **kwargs) -> NotImplemented:
        raise NotImplementedError

class APIDriver(BaseAPIDriver):
    def __init__(self, version: str) -> NoReturn:
        super().__init__(version)

    def call_action(self, action: str, headers: dict, *, params: dict = {}, method: str = "get") -> requests.Response:
        response = requests.request(
            method=method,
            url=self.__generate_action_url__(action),
            headers=headers,
            params=params
        )
        return response