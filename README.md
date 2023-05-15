# Donatello.py


![Made with Python](https://img.shields.io/badge/Made%20with-Python-%23FFD242?logo=python&logoColor=white)
![MIT License](https://img.shields.io/badge/License-MIT-blue.svg)
![Version: 1.0.7](https://img.shields.io/badge/version-1.0.7-red)
![PyPI - Downloads](https://img.shields.io/pypi/dm/donatello?color=succeses&logo=Pypi&logoColor=white)

🐍 Unofficial Python wrapper for working with the API of the Ukrainian service for donations [Donatello](https://donatello.to/)

[GitHub](https://github.com/selfkilla666/donatello/) | [PyPI](https://pypi.org/project/donatello/) | [Discord server](https://discord.gg/donatello-498101952333479956)
<br>

---

## Quickstart

Before you start, you need to take a couple of steps
1) First you need to create a Donatello token and enable the API functionality, all this can be done in your account on the API page
2) You need to install the library via `pip install donatello`

### Get me as User

If you need to get information about the user with which you authenticated through a token, then this can be done through the convenient `get_me()` method

```python

from donatello import Donatello


token = "<YOUR TOKEN HERE>"
client = Donatello(token)

me = client.get_me()

# Print your account nickname
print(me.nickname)

```

### Get donations

You may need to get a list of your donations, and there is a `get_donates()` method specifically for this, which will return you a convenient list of them

```python

from donatello import Donatello


token = "<YOUR TOKEN HERE>"
client = Donatello(token)

donates = client.get_donates(size = 5) # "size = 5" - Get 5 last donates

for donate in donates:
    print(f"{donate.client_name}: {donate.message}")

```
    
### Get top donators

You can get top donators using the `get_clients()` method

```python

from donatello import Donatello


token = "<YOUR TOKEN HERE>"
client = Donatello(token)

donators = client.get_clients()

for donator in donators:
    print(f"{donator.client_name}: {donator.total_amount}")


```

---

## In future

- [ ] Add async API driver
- [ ] Add docs
- [ ] Longpolling / Events
