# Donatello API


![Made with Python](https://img.shields.io/badge/Made%20with-Python-%23FFD242?logo=python&logoColor=white)
![MIT License](https://img.shields.io/badge/License-MIT-blue.svg)
![Version: 1.0.2](https://img.shields.io/badge/version-1.0.2-white)
![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)

🐍 Unofficial Python wrapper for working with the API of the Ukrainian service for donations [Donatello](https://donatello.to/)

You can support the developer [here](https://donatello.to/selfkilla666) =)

## Quickstart

Before you start, you need to take a couple of steps
1) First you need to create a Donatello token and enable the API functionality, all this can be done in your account on the API page
2) You need to install the library via `pip install donatello_api`

### Get me as User

If you need to get information about the user with which you authenticated through a token, then this can be done through the convenient `get_me()` method

```python

from donatello_api import Donatello


token = "<YOUR TOKEN HERE>"
client = Donatello(token)

me = client.get_me()

print(me.nickname)

```

### Get donations

You may need to get a list of your donations, and there is a `get_donates()` method specifically for this, which will return you a convenient list of them

```python

from donatello_api import Donatello


token = "<YOUR TOKEN HERE>"
client = Donatello(token)

donates = client.get_donates(size = 5)

for donate in donates:
    print(f"{donate.client_name}: {donate.message}")

```

## In future

- [ ] Add async API driver
- [ ] Add docs
- [ ] Longpolling / Events
- [ ] Support new features in Donatello API 
