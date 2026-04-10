# 1.
class Cat:
    def speak(self):
        return "Welcome to Cat"

class Dog:
    def speak(self):
        return "Welcome to Dog"

class Duck:
    def speak(self):
        return "Welcome to Duck"

animals = [Cat(), Dog(), Duck()]
for animal in animals:
    print(animal.speak())


# 2.
class Shape:
    def get_pr(self):
        pass

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def get_pr(self):
        return 4 * self.side

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_pr(self):
        return 2 * (self.width + self.height)

class Triangle(Shape):
    def __init__(self, side1, side2, side3):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def get_pr(self):
        return self.side1 + self.side2 + self.side3

shapes = [Square(2), Rectangle(3,5), Triangle(2, 3, 3)]
for shape in shapes:
    print(f"Периметр: {shape.get_pr()}")


# 3.
from abc import ABC, abstractmethod

class Shape(ABC):

    @abstractmethod
    def get_pr(self):
        pass

try:
    shape = Shape()
    print(shape.get_pr())
except Exception as e:
    print(e)


# 4.
class A:
    def __init__(self):
        print("init A")

class B:
    def __init__(self):
        print("init B")

class C:
    def __init__(self):
        print("init C")

class D(A,B,C):
    def __init__(self):
        super().__init__()
        print("init D")

obj = D()

print(D.__mro__)


# 5.
class MixinLog:
    ID = 0

    def __init__(self):
        MixinLog.ID += 1
        self.id = MixinLog.ID

class HotelBooking:

    def __init__(self, room, price, date):
        self.room = room
        self.price = price
        self.date = date
        print(f"Бронирование: номер {room}, цена {price}, дата заезда {date}")

    def show_booking_details(self):
        print(f"Детали бронирования:")
        print(f"- Номер комнаты: {self.room}")
        print(f"- Цена: {self.price}$")
        print(f"- Дата: {self.date}")

class BookingWithLog(HotelBooking, MixinLog):
    def __init__(self, room, price, date):
        HotelBooking.__init__(self, room, price, date)
        MixinLog.__init__(self)

booking = BookingWithLog(room=101, price=150, date="2023-08-18")

booking.show_booking_details()

print(f"Уникальный ID бронирования: {booking.id}")


# 6.
class Goods:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def print_info(self):
        print(f"Name: {self.name}, Price: {self.price}")

class MixinLog:
    ID = 0

    def __init__(self):
        self.ID += 1
        self.id = MixinLog.ID

    def print_info(self):
        print(f"Лог-запись: ID = {self.id}")


class Notebook1(Goods, MixinLog):
     pass

class Notebook2(MixinLog, Goods):
    pass

n1 = Notebook1 ( "MSI", 29_000 )
n1.print_info()

n2 = Notebook2()
n2.print_info()

# 7.
class Calculator:

    def divide(self, numerator, denominator):
       try:
            result = numerator / denominator
            return result
       except ZeroDivisionError:
            return "На ноль делить нельзя!"

numerator = float(input("Введите делимое число: "))
denominator = float(input("Введите делитель: "))

calc = Calculator()
result = calc.divide(numerator, denominator)
print(result)


def division(numerator, denominator):
    try:
        return numerator / denominator
    except ZeroDivisionError:
        return "На ноль делить нельзя!"

numerator = float(input("Введите делимое число: "))
denominator = float(input("Введите делитель: "))

result = division(numerator, denominator)
print(result)

numerator = float(input("Введите делимое число: "))
denominator = float(input("Введиет делитель:"))
if denominator == 0:
    print(f"На ноль делить нельзя!")
else:
    result = numerator / denominator
    print(result)

numerator = float(input("Введите делитель: "))
denominator = float(input("Введите делимое число: "))
try:
       result = numerator / denominator
       print(result)
except ZeroDivisionError:
       print("На ноль делить нельзя!")

# 8.
class Calculator:

    def divide(self, numerator, denominator):
       try:
            result = numerator / denominator
            return result
       except ZeroDivisionError:
            return "На ноль делить нельзя!"

try:
    numerator = float(input("Введите делимое число: "))
    denominator = float(input("Введите делитель: "))

    calc = Calculator()
    result = calc.divide(numerator, denominator)
    print(result)

except ValueError:
    print("Ошибка ввода: введите числа")

# 9.
class Calculator:
    def divide(self, numerator, denominator):
        try:
            result = numerator / denominator
            return result
        except ZeroDivisionError:
            return "На ноль делить нельзя!"

try:
    numerator = float(input("Введите делимое число: "))
    denominator = float(input("Введите делитель: "))

    calc = Calculator()
    result = calc.divide(numerator, denominator)
    print(result)

except ValueError:
    print("Ошибка: введите число!")
except Exception :
    print(f"Произошла неизвестная ошибка")


# 10.
class Calculator:
    def divide(self, numerator, denominator):
        try:
            result = numerator / denominator
            return result
        except ZeroDivisionError as e:
            return f"Ошибка: {e}"

try:
    numerator = float(input("Введите делимое число: "))
    denominator = float(input("Введите делитель: "))

    calc = Calculator()
    result = calc.divide(numerator, denominator)
    print(result)

except ValueError as e:
    print(f"Ошибка: {e}")
except Exception as e:
    print(f"Произошла неизвестная ошибка: {e}")

11.
try:
    numerator = float(input("Введите делимое число: "))
    denominator = float(input("Введите делитель: "))
    result = numerator / denominator

except ArithmeticError as e:
    print(f"Арифметическая ошибка: {type(e).__name__}:{e}\n")

# 12.
try:
    numerator = float(input("Введите делимое число: "))
    denominator = float(input("Введите делитель: "))

    result = numerator / denominator
    print(f"Результат: {result}")
except ZeroDivisionError:
    print("Ошибка: деление на ноль!")
except ValueError:
    print("Ошибка: введите числа, а не буквы!")
except Exception as e:
    print(f"Неизвестная ошибка: {e}")
else:
    print("Деление выполнено успешно")

# 13.
try:
    numerator = float(input("Введите делимое число: "))
    denominator = float(input("Введите делитель: "))

    result = numerator / denominator
    print(f"Результат: {result}")
except ZeroDivisionError:
    print("Ошибка: деление на ноль!")
except ValueError:
    print("Ошибка: введите числа, а не буквы!")
except Exception as e:
    print(f"Неизвестная ошибка: {e}")
else:
    print("Деление выполнено успешно")

finally:
    print("Работа программы завершена")

# 14.
try:
    numerator = float(input("Введите делимое число: "))
    denominator = float(input("Введите делитель: "))

    try:
       result = numerator / denominator
       print(f"Результат: {result}")
    except ZeroDivisionError:
       print("Ошибка: деление на ноль!")

except ValueError:
    print("Ошибка: введите числа, а не буквы!")

# 15.
def divide(x, y):
    try:
        result = x / y
        return result
    except ZeroDivisionError:
        return "Ошибка: деление на ноль!"

try:
    numerator = float(input("Введите делимое число: "))
    denominator = float(input("Введите делитель: "))

    result = divide(numerator, denominator)
    print(result)

except ValueError:
    print("Ошибка: введите числа, а не буквы!")
