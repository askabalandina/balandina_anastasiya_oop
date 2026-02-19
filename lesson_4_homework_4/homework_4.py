# 1.
class SecureData:
    def __init__(self, secret):
        self.__secret = secret

    def __getattribute__(self, name):
        if name == '__secret':
            raise ValueError("Доступ запрещен!")
        return super().__getattribute__(name)

    def get_secret(self):
        return self.__secret  # внутри класса доступ работает


data = SecureData("пароль123")

# print(data.__secret)
print(data.get_secret())


class SecureData:
    def __init__(self, secret):
        self.__secret = secret

    def __getattribute__(self, name):
        if name == "secter":
            raise ValueError("Доступ запрещен")
        return object.__getattribute__(self, name)  #объясни, пожалуйста, не выпадает ошибка при испол. object?

    def get_secret(self):
        return self.__secret
data = SecureData('пароль123')

print(data.__secret)
print(data.get_secret())

# 2.
class SecureData:
    def __init__(self, secret):
        self.__secret = secret

    def __getattribute__(self, name):
        if name == '__secret':
            raise ValueError("Доступ запрещен!")
        return super().__getattribute__(name)

    def get_secret(self):
        return self.__secret

    def __setattr__(self, name, value):
        if name == 'token':
            raise ValueError("Нельзя создавать")
        return super().__setattr__(name, value)

data = SecureData("пароль123")

data.token = 'abc123'
print(data.token)

data.other = 'ok'
print(data.other)

# 3.
class SafeDict:
    default = None

    def __getattr__(self, name):
           return f"N/A"

    def __delattr__(self, name):
        print(f"удален атрибут х {name}")
        super().__delattr__(name)

d = SafeDict()
print(d.unknown)

d.key = 10
del d.key


# 4.
class Employee:

    def __init__(self, name, salary):
        self.__name = name
        self.__salary = salary

    @property
    def salary(self):
        return self.__salary

    @salary.setter
    def salary(self, salary):
        if salary < 0:
            raise ValueError(f"Зарплата не может быть отрицательной")
        self.__salary = salary
        print(f"Зарплата обновлена: {salary}")

    @property
    def name(self):
        return self.__name

e = Employee("Daniil", 5000)
print(e.salary)
e.salary = 8000
print(e.salary)
e.salary = -100

# 5.
class Employee:
    def __init__(self, name, salary):
        self._name = name
        self._salary = salary

    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self, salary):
        if salary < 0:
            raise ValueError("Зарплата не может быть отрицательной")
        self._salary = salary
        print(f"Зарплата обновлена: {salary}")

    @salary.deleter
    def salary(self):
        print("Зарплата удалена")
        del self._salary

    @property
    def name(self):
        return self._name

e = Employee("Daniil", 45000)
# print(e.salary)

del e.salary
print(e.__dict__)

# 6.
class LoginForm:

    def __init__(self, username):
        self.username = username

    @property
    def username(self):
        return self._username

    @username.setter
    def username(self, value):
        print(f"username изменен на '{value}'")
        self._username = value

form = LoginForm("admin1")

form.username = "admin5"
print(form.username)

# 7.
import logging
from datetime import datetime

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')

class Card:
    def __init__(self, number):
        self.number = number

    @property
    def number(self):
       masked_number = f"**** **** **** {self.__number[-4:]}"
       return masked_number

    @number.setter
    def number(self, value):
        if len(value) != 16 or not value.isdigit():
            raise ValueError("Номер карты должен содержать 16 цифр")
        self._Card__number = value

    @number.deleter
    def number(self):
        current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        logging.info(f'Удалён номер карты в {current_time}')
        del self._Card__number

try:
    card = Card('1234567890123456')
    print(card.number)

    try:
        card.number = 'abc'
    except ValueError as e:
        print(e)

    del card.number
except Exception as ex:
    print(ex)

# 8.
class UserData:

    def __init__(self, email, age, is_active):
        if '@' not in email:
            raise ValueError("Email должен содержать символ '@'")

        if age < 18:
            raise ValueError("Пользователь должен быть старше 18 лет")


        self.email = email
        self.age = age
        self.is_active = bool(is_active)

    @property
    def json(self):
        return {'email': self.email, 'age': self.age, 'is_active': self.is_active}


def test_UserData():
    try:
        valid_user = UserData('test1@mail.ru', 20, True)
        assert valid_user.json == {'email': 'test1@mail.ru', 'age': 20, 'is_active': True}

        invalid_email_user = UserData('invalid_email1mail.ru', 20, True)
    except ValueError as err:
        assert str(err) == "Email должен содержать символ '@'"

    try:
        young_user = UserData('testyoung@mail.ru', 15, True)
    except ValueError as err:
         assert str(err) == "Пользователь должен быть старше 18 лет"

test_UserData()
print("Тесты пройдены")

