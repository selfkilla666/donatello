
import unittest
from donatello import Donatello

try:
    from os import environ
    from dotenv import load_dotenv

    load_dotenv()
except ImportError:
    print("Please, for test install dotenv lib `pip install python-dotenv`")


class TestGetClients(unittest.TestCase):
    def test_get_clients(self):

        token = environ.get("TOKEN", default=lambda x: Exception("No TOKEN in `.env` file"))
        client = Donatello(token)

        donators = client.get_clients()
        top_donator = donators[0]

        self.assertEqual(top_donator.client_name, "selfkilla666")
        self.assertEqual(top_donator.total_amount, 88)