# 1.
import math
from turtle import Shape

class Shape:
    def area(self):
        return 0

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
            return math.pi * self.radius ** 2

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
            return self.side ** 2

c = Circle(5)
s = Square(4)

print(c.area())
print(s.area())

# 2.
class BasePage:

    def open(self, url):
        print(f"Открываем страницу {url}")

    def __init__(self ):
        self.text = "Зима"

class LoginPage(BasePage):
    def find(self, text):
        if text in self.text:
            print(f"На странице найден текст: \"{text}\"")
        else:
            print(f"Текст \"{text}\" не найден на странице.")

page = LoginPage()
page.open("https://example.com/login")
page.find("мир")

# 3.
class ResultList(list):

    def success_count(self):
        count = sum(1 for item in self if item.get("status") == "passed")
        return count

results = ResultList([
    {"status": "passed"},
    {"status": "failed"},
    {"status": "passed"},
])

print(results.success_count())

# 4.
class BaseStep:
    pass

class LoginStep(BaseStep):
    pass
step = LoginStep()

print(issubclass(LoginStep, BaseStep))
print(isinstance(step, BaseStep))
print(isinstance(step, object))

# 5.
class ExtendedDict(dict):
    def __str__(self):
        items = []
        for key, value in self.items():
            items.append(f"{key}: {value}")
        return "\n".join(items)

d = ExtendedDict(a=1, b=2)
print(d)


# 6.
class Widget:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Button(Widget):
    def __init__(self, x, y, label):
        super().__init__(x, y)
        self.label = label


btn = Button(100, 200, "OK")

print(btn.x, btn.y, btn.label)

# 7.
class Widget:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Button(Widget):
    def __init__(self, x, y, label):
        self.label = label

btn = Button(100, 200, "OK")

print(btn.__dict__)

# 8.
class Logger:
    def log(self, msg):
        print(msg)

class HTMLLogger(Logger):
    def log(self, msg):
        super().log(msg)
        print(f"<p>{msg}</p>")

logger = HTMLLogger()
logger.log("Login successful")
