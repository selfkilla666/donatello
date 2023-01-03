# Donatello.py


![Made with Python](https://img.shields.io/badge/Made%20with-Python-%23FFD242?logo=python&logoColor=white)
![MIT License](https://img.shields.io/badge/License-MIT-blue.svg)
![Version: 1.0.5](https://img.shields.io/badge/version-1.0.5-white)
![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)
![PyPI - Downloads](https://img.shields.io/pypi/dm/donatello?color=succeses&logo=Pypi&logoColor=white)
![Python version: 3.7 | 3.8 | 3.9 | 3.10 | 3.11](https://img.shields.io/pypi/pyversions/donatello_api?color=blue&label=Python%20version)

🐍 Неофіційна бібліотека Python для роботи з українським сервісом донатів [Donatello](https://donatello.to/)

[GitHub](https://github.com/selfkilla666/donatello/) | [PyPI](https://pypi.org/project/donatello/) | [Discord server](https://discord.gg/donatello-498101952333479956)
<br>
[English version](https://github.com/selfkilla666/donatello/blob/main/README.md)

---

## Швидкий старт

Перед початком вам потрібно зробити декілька кроків
1) Вам потрібно увімкнути функціонал API та отримати ваш токен для роботи з ним. Усе це можна зробити у налаштуванні, у вкладці "**Про API**".
2) Інсталювати бібліотеку для роботи з API, використавши команду `pip install donatello` у консолі.

### Отримати інформацію про себе

Якщо вам потрібно отримати інформацію про себе, або авторизованого користувача за токеном, то ви це можете зробити за допомогою метода `get_me()`

```python

from donatello import Donatello


token = "<Ваш токен тут>"
client = Donatello(token)

me = client.get_me()

# Виведе у консоль ваш нікнейм
print(me.nickname)

```

### Отримати список донатів

Ви можете легко отримати список останніх донатів за допомогою метода `get_donates()`

```python

from donatello import Donatello


token = "<Ваш токен тут>"
client = Donatello(token)

# size = 5 - отримати останні 5 донатів
donates = client.get_donates(size = 5)

for donate in donates:
    print(f"{donate.client_name}: {donate.message}")

```

### Топ донатерів

Ви можете отримати топ донатерів за допомогою метода `get_clients()`

```python

from donatello import Donatello


token = "<Ваш токен тут>"
client = Donatello(token)

donators = client.get_clients()

for donator in donators:
    print(f"{donator.client_name}: {donator.total_amount}")

```

---

## У майбутньому

- [ ] Додати асинхронний клієнт
- [ ] Документація
- [ ] Лонгполінг / Івенти
- [ ] Додавати нові функції з Donatello API 
