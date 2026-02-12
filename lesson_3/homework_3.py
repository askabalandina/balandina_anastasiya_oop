# 1.
class Circle:
    MIN_RADIUS = 1
    MAX_RADIUS = 1000

    @classmethod
    def is_valid_radius(cls, r):
        return cls.MIN_RADIUS <= r <= cls.MAX_RADIUS

print(Circle.is_valid_radius(500))
print(Circle.is_valid_radius(1500))


# 2.
import math
class Circle:
    MIN_RADIUS = 1
    MAX_RADIUS = 1000

    @classmethod
    def is_valid_radius(cls, r):
        return cls.MIN_RADIUS <= r <= cls.MAX_RADIUS

    @staticmethod
    def area(radius):
        return math.pi * radius ** 2

    def __init__(self, radius):
        if Circle.is_valid_radius(radius):
            self.radius = radius

c = Circle(4)

print(c.area(c.radius))


# 3.
import math
class Circle:
    MIN_RADIUS = 1
    MAX_RADIUS = 1000

    @classmethod
    def is_valid_radius(cls, r):
        return cls.MIN_RADIUS <= r <= cls.MAX_RADIUS

    @staticmethod
    def area(radius):
        return math.pi * radius ** 2

    def __init__(self, radius):
        if Circle.is_valid_radius(radius):
            self.radius = radius

    def print_info(self):
        circle_class = type(self)
        print(f"Радиус: {self.radius}")
        print(f"Допустимый диапазон: [{circle_class.MIN_RADIUS}, {circle_class.MAX_RADIUS}]")

c = Circle(4)

c.print_info()


# 4.
class User:
    def __init__(self):
        self.__login = None
        self.__password = None

    def set_credentials(self, login, password):
        if isinstance(login, str) and isinstance(password, str):
            self.__login = login
            self.__password = password

    def get_credentials(self):
        return self.__login, self.__password

u = User()
u.set_credentials("example_user", "secure_password12")
print(u.get_credentials())


# 5.
class User:
    def __init__(self):
        self.__login = None
        self.__password = None

    def __encrypt_password(self, password):
        return password.upper()

    def set_credentials(self, login, password):
        if isinstance(login, str) and isinstance(password, str):
            self.__login = login
            self.__password = self.__encrypt_password(password)

    def check_password(self, password):
        encrypted_password = self.__encrypt_password(password)
        return encrypted_password == self.__password

    def get_credentials(self):
        return self.__login, self.__password

u = User()
u.set_credentials("daniil", "qwerty")

print(u.check_password("qwerty"))
print(u.check_password("QWERTY"))
print(u.check_password("qwe"))


# 6.
class User:
    def __init__(self):
        self.__login = None
        self.__password = None

    def __encrypt_password(self, password):
        return password.upper()

    def set_credentials(self, login, password):
        if isinstance(login, str) and isinstance(password, str):
            self.__login = login
            self.__password = self.__encrypt_password(password)

    def check_password(self, password):
        encrypted_password = self.__encrypt_password(password)
        return encrypted_password == self.__password

    def get_credentials(self):
        return self.__login, self.__password

u = User()
u.set_credentials("daniil", "qwerty")

print(u.check_password("qwerty"))

try:
    print(u.encrypt_password("secret"))
except AttributeError as e:
    print(e)

try:
    print(u.__password)
except AttributeError as e:
    print(e)

print(u._User__password)