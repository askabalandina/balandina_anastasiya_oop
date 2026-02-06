# 1.
class Person:
    def set_data(self, name, age):
        self.name = name
        self.age = age

    def get_data(self):
        return f"Имя: {self.name}, Возраст: {self.age}"

person_1 = Person()
person_2 = Person()

person_1.set_data("Иван", 25)
person_2.set_data("Анна", 23)

print(person_1.get_data())
print(person_2.get_data())


# 2.
class Point:
    def set_coords(self, x, y):
        self.x = x
        self.y = y

    def get_coords(self):
        return self.x, self.y

p = Point()
p.set_coords(7, 12)
print(p.get_coords())

p.set_coords(-3, 5)
print(p.get_coords())


# 3.
class Point:
    def set_coords(self, x, y):
        self.x = x
        self.y = y

    def get_coords(self):
        return self.x, self.y

p = Point()
p.set_coords(40, 70)
print(getattr(p, 'get_coords')())
print(p.get_coords())


# 4.
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show_info(self):
        return f"Имя: {self.name}, возраст: {self.age}"

info_person = Person("Иван", 34)
print(info_person.show_info())


# 5.
class Person:
    def __init__(self, name):
        self.name = name

    def _del_(self):
       return f"Удален объект: {self.name}"

p_name_1 = Person("Иван")
p_name_2 = Person("Анна")
p_name_3 = Person("Максим")

del p_name_1
del p_name_2

print(f"p_name_3: {p_name_3.name}")


# 6.
class Rectangle:
    def __init__(self, width = 1, height = 1):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

rectangle_1 = Rectangle()
print(rectangle_1.area())

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

rectangle_2 = Rectangle(2, 6)
print(rectangle_2.area())

# 7.
class Logger:
    isinstance = None

    def __new__(cls, *args, **kwargs):
        if cls.isinstance is None:
            cls.isinstance = super().__new__(cls)
        print(f"Создание логгера")

    def __init__(self):
        print(f"Инициализация логгера")

logger_1 = Logger()
logger_2 = Logger()

