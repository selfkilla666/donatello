
import unittest
from donatello import Donatello

try:
    from os import environ
    from dotenv import load_dotenv

    load_dotenv()
except ImportError:
    print("Please, for test install dotenv lib `pip install python-dotenv`")


class TestGetDonates(unittest.TestCase):
    def test_get_donates(self):

        token = environ.get("TOKEN", default=lambda x: Exception("No TOKEN in `.env` file"))
        client = Donatello(token)

        donates = client.get_donates(size=5)
        last_donate = donates[0]

        self.assertEqual(donates.size, 5)
        self.assertEqual(donates.total, 1)
        self.assertEqual(last_donate.client_name, "selfkilla666")
        self.assertEqual(last_donate.amount, 88)
        self.assertEqual(last_donate.currency, "UAH")