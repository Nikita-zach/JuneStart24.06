#Task 1
class BalanceDescriptor:
    def __get__(self, instance, value):
        return instance._Account__balance

    def __set__(self, instance, value):
        raise AttributeError("Balance cannot be changed after initialization.")

class Account:
    balance = BalanceDescriptor()

    def __init__(self, balance):
        self.__balance = balance

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, value):
        self.__balance = value

    def __getattr__(self, item):
        return f"There is no attribute such as '{item}'"

    def __setattr__(self, key, value):
        if key == 'balance':
            raise AttributeError("Balance cannot be changed after initialization.")
        if value <= 0:
            raise ValueError("Balance cannot negative nor equal to zero.")
        if not isinstance(value, int | float):
            raise TypeError("Balance must be an integer or float.")
        super().__setattr__(key, value)



x = Account(1000)
print(x.balance)
try:
    x.balance = - 100
except Exception as e:
    print(e)
print(x.balance)
print(x.name)

#Task 2
class User:
    def __init__(self, first_name, last_name):
        self.__first_name = first_name
        self.__last_name = last_name

    @property
    def first_name(self):
        return self.__first_name

    @first_name.setter
    def first_name(self, value):
        self.__first_name = value

    @property
    def last_name(self):
        return self.__last_name

    @last_name.setter
    def last_name(self, value):
        self.__last_name = value

    def __getattr__(self, item):
        return f"There's is no such attribute as {item}"

    def __setattr__(self, key, value):
        if key == "_User__first_name" or key == "_User__last_name":
            if not isinstance(value, str):
                raise TypeError("Value of a attribute must be a string type.")
            if value == "":
                raise ValueError("Value of a attribute cannot be empty.")
            return super().__setattr__(key, value)
        print(f"Attribute {key} is already set and cannot be changed!")


user1 = User('John', 'Doe')
user1.first_name = 'Jane'
print(user1.first_name)
print(user1.fullname)

#Task 3
class Rectangle:
    def __init__(self, width, height):
        self.__width = width
        self.__height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        self.__width = value

    @property
    def height(self):
       return self.__height

    @height.setter
    def height(self, value):
        self.__height = value

    @property
    def area(self):
        return self.__width * self.__height


    def __getattr__(self, item):
        return f"There's is no such attribute as {item}"

    def __setattr__(self, key, value):
        if key == "_Rectangle__width" or key == "_Rectangle__height":
            if not isinstance(value, int | float):
                raise TypeError("Value of a attribute must be an integer or float")
            if value <= 0:
                raise ValueError(f"Value of a attribute must be greater than 0")
            return super().__setattr__(key, value)
        print(f"Attribute {key} is already set and cannot be changed!")

z = Rectangle(5, 5)
z.width = 100
print(z.width)
print(z.length)
print(z.area)