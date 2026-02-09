# 1.
class Dog:
    species = "canis"
    legs = 4
    color = "grey"
    hairy = "long-haired"

Dog.color = "brown"

print(" Color: ", Dog.color)

print("All attr:", Dog.__dict__)


# 2.
class Dog:
    """Dog - класс, описывающий собаку.
    Собаки относятся к роду "canis" и имеют 4 лапы."""

    species = "canis"
    legs = 4

setattr(Dog, 'name', 'Dic')
setattr(Dog, 'age', '2')

print('All attr:',Dog.__dict__)

print(Dog.__doc__)
help(Dog)


# 3.
class User:
    role = "guest"
    active = True

setattr(User, 'role', 'admin')
print(hasattr(User, 'active'))
setattr(User, 'email', 'test1@example.com')
print(User.role)
print(User.email)

print("All attr: ", User.__dict__)