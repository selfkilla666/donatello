
from __future__ import annotations
from requests import request
from requests.models import Response

from donatello.driver import BaseAPIDriver


class APIDriver(BaseAPIDriver):
    def __init__(self, version: str) -> None:
        super().__init__(version)

    def call_action(self, action: str, headers: dict, *, params: dict = {}, method: str = "get") -> Response:
        response = request(
            method=method,
            url=self.__generate_action_url__(action),
            headers=headers,
            params=params
        )
        return response