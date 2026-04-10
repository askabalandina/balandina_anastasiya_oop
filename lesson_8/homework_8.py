# 1.
def inner():
    result = 9 / 0
    return result

def outer():
    inner()

outer()

def inner(numerator):
    result = numerator / 0
    return result

def outer():
    inner(10)

outer()


# 2.
def inner():
    numerator = int(input("Введите число: "))
    result = numerator / 0
    return result

def outer():
       inner()
try:
    outer()
except Exception as e:
    print("Ошибка перехвачена на верхнем уровне")

# 3.
def inner():
    try:
       numerator = int(input("Введите число: "))
       result = numerator / 0
       return result
    except:
        return "Ошибка в inner"

def outer():
       return inner()

result = outer()
print(result)

# 4.
def inner():
    numerator = int(input("Введите число: "))
    result = numerator / 0
    return result

def outer():
    try:
        inner()
    except:
        print("Ошибка в outer")

outer()

# 5.
def get_value():
    raise ValueError()

def test_get_value():
    try:
        get_value()
    except ValueError:
        assert False

test_get_value()

# 6.
def divide(x, y):
    if y == 0:
        raise ZeroDivisionError("Делить на ноль нельзя!")
    else:
        result = x / y
        return result

print(divide(8,0))

# 7.
class NegativeNumberError(Exception):
    pass

def sqrt(x):
    if x < 0:
        raise NegativeNumberError("Корень из отрицательного числа")
    return x ** (1 / 2)

try:
    print(sqrt(1))
    print(sqrt(-2))
except NegativeNumberError as e:
    print(e)

# 8.
class MathError(Exception):
    pass

class NegativeNumberError(MathError):
    pass

class DivisionByZeroError(MathError):
    pass

def safe_divide(x, y):
    if y == 0:
        raise DivisionByZeroError("На ноль делить нельзя!")
    return x / y

try:
    result = safe_divide(10, 0)
    print("Результат:", result)

except MathError as error:
    print(f"Математическая ошибка: {error}")

# 9.
import math

class NegativeNumberError(Exception):
    pass

def sqrt(x):
    if x < 0:
        raise NegativeNumberError("Нельзя брать корень из отрицательного числа")
    return math.sqrt(x)

def test_sqrt():
    try:
        sqrt(-5)
    except NegativeNumberError:
        return
    except Exception as e:
        assert False, f"Ожидалось NegativeNumberError, но получено: {type(e).__name__}"

    assert False, "Нельзя брать корень из отрицательного числа"

test_sqrt()
print("Тест пройден успешно")

10.
with open('sample.txt', 'r', encoding='utf-8') as file:
    print(file.read())


# 11.
class BackupList:
    def __init__(self, original_list):
        self.original_list = original_list
        self.backup = None

    def __enter__(self):
        self.backup = self.original_list.copy()
        return self.original_list

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is not None:
            self.original_list[:] = self.backup
            print("Произошла ошибка, изменения отменены.")
            return True
        return False

my_list = [1, 2, 3]
print("Исходный список:", my_list)
with BackupList(my_list) as lst:
    lst.append(4)
    lst[0] = 10
print("После успешного изменения:", my_list)

my_list = [1, 2, 3]
print("\nИсходный список:", my_list)
try:
    with BackupList(my_list) as lst:
        lst.append(4)
        raise ValueError("Что-то пошло не так!")
except ValueError as e:
    print("Исключение перехвачено:", e)
print("После ошибки (должен быть откат):", my_list)


# 12.
import time

class Timer:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        start_time = time.time()
        result = self.func(*args, **kwargs)
        end_time = time.time()
        elapsed = end_time - start_time

        print(f"Функция {self.func.__name__} выполнялась {elapsed:.5f} секунд")
        return result

@Timer
def пример_функции():

    time.sleep(1)
    print("Функция выполнена!")

пример_функции()