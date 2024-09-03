#Task 1
def pre_and_post_func():
    def decorator(func):
        def func_wrapper(*args):
            return f"{stars()}\n{func(*args)}\n{stars()}"
        return func_wrapper
    return decorator

@pre_and_post_func()
def greetings(name):
    return f"Hello, {name}!"
def stars(n = 10):
    return "*" * n

print(greetings("Bob"))

#Task 2

from random import randint


def log_decorator():
    def decorator(func):
        def wrapper(arg1):
            with open("buff.txt","w",encoding="utf-8") as f:
                return f.write(str(func(arg1)))
        return wrapper
    return decorator

@log_decorator()
def rand_num(n):
    return randint(n, n * 10)

rand_num(5)

#Task 3
def exception_catcher():
    def decorator(func):
        def wrapper(*args):
            try:
                func(args)
            except Exception as e:
                raise e
        return wrapper
    return decorator

@exception_catcher()
def divide(a, b):
    return a / b

divide(5, 0)

#Task 4

import timeit

def t_counter():
    def decorator(func):
        def wrapper(*args):
            execution_time = timeit.timeit(lambda: func(*args), number=20)
            return execution_time
        return wrapper
    return decorator

@t_counter()
def factorial(n):
    if n == 0 or n == 1:
        return n
    return n * factorial(n - 1)

print(f"Execution time: {factorial(5)}")

#Task 5


def log_func_decorator():
    def decorator(func):
        def wrapper(arg1):
            with open("buff.txt","w",encoding="utf-8") as f:
                return f.write(f"function: {func.__name__}\narguments: {arg1}\nresult: {func(arg1)}")
        return wrapper
    return decorator

@log_decorator()
def rand_num(n):
    return randint(n, n * 10)

rand_num(5)

#Task 6
def call_limit(limit):
    def decorator(func):
        n = 0
        def wrapper(*args):
            nonlocal n
            n += 1
            if n > limit:
                return "This function was used to many times, that's more than enough"
            else:
                return func(*args)
        return wrapper
    return decorator

@call_limit(3)
def say_hello(name):
    return f'Hello,{name}'

for _ in range(5):
    print(say_hello('John'))

#Task 7
def cache_decorator():
    def decorator(func):
        cache = {}

        def wrapper(*args):
            if args in cache:
                return cache[args]
            else:
                cache[args] = func(*args)
                return cache[args]

        return wrapper

    return decorator


@cache_decorator()
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


print(fibonacci(10))
print(fibonacci(10))