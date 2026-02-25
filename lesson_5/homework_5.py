# 1.
class LengthValidator:

    def __init__(self, min_len, max_len):
        self.min_len = min_len
        self.max_len = max_len

    def __call__(self, value):
        if self.min_len <= len(value) <= self.max_len:
            return True
        else:
            raise ValueError ("Длина переданной строки вне допустимого диапазона")

validator = LengthValidator(3, 10)
print(validator("python"))
print(validator("hi"))


# 2.
class Sumator:
    def __init__(self):
        self.total = 0

    def  __call__(self, number):
        self.total += number
        return self.total

    def __str__(self):
        return f"Сумма: {self.total}"

s = Sumator()
print(s(5))
print(s(10))
print(s(-2))
print(s)

# 3.
class HasText:
    def __init__(self, line_text):
        self.line_text = line_text
    def __call__(self, text):
        return self.line_text in text

try:
    assert HasText("Success")("Test passed: Success")
    print("Первый assert прошел")
except AssertionError:
    print("Первый assert не прошел")

try:
    assert HasText("Error")("All OK")
    print("Второй assert прошел")
except AssertionError:
    print("Второй assert не прошел")

# 4.
class Book:
    def __init__(self,title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return f"{self.author} - {self.title}"

    def __repr__(self):
        return f"<Book '{self.title}' by {self.title}>"

book = Book("1984", "Джордж Оруэлл")
print(book)
print(repr(book))

# 5.
class TestUser:

    def __init__(self, id, name, email):
        self.id = id
        self.name = name
        self.email = email

    def __repr__(self):
        return f"<TestUser(id={self.id}, name={self.name}, email={self.email})>"

user = TestUser(12, "Daniil", "daniil@example.com")
print(user)