
import unittest
from donatello_api import Donatello

try:
    from os import environ
    from dotenv import load_dotenv

    load_dotenv()
except ImportError:
    print("Please, for test install dotenv lib `pip install python-dotenv`")


class TestGetMe(unittest.TestCase):
    def test_get_me(self):

        token = environ.get("TOKEN", default=lambda x: Exception("No TOKEN in `.env` file"))
        client = Donatello(token)

        me = client.get_me()

        self.assertEqual(me.nickname, "selfkilla666")
        self.assertEqual(me.id, "C2203-5702")
        self.assertEqual(me.is_public, True)
        self.assertEqual(me.page, "https://donatello.to/selfkilla666")