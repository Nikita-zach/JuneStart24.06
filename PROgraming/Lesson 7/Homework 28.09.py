#Task 1
def func_prog(start, n):
    current = start

    def inner(func):
        curr = func(current)
        for _ in range(n):
            yield curr
            curr = func(curr)

    return inner


def plus_1(x):
    return x + 1


def mul_by_2(x):
    return x * 2


z = func_prog(4, 10)
arif_gen = z(plus_1)
geom_gen = z(mul_by_2)
for item in arif_gen:
    if item > 10:
        arif_gen.close()
    print(item, end="\t")
print()
for item in geom_gen:
    if item > 100:
        geom_gen.close()
    print(item, end="\t")

#Task 2

import timeit


def fibonacci_iter():
    buff = [0, 1]

    def inner(n):
        for _ in range(n):
            buff.append(buff[-2] + buff[-1])
        return buff[-2]

    return inner


def fibonacci_rec(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_rec(n - 1) + fibonacci_rec(n - 2)


x = fibonacci_iter()
print(x(20))
print(fibonacci_rec(20))

iter_time = timeit.timeit('x(20)', globals=globals(), number=1000)
rec_time = timeit.timeit('fibonacci_rec(20)', globals=globals(), number=1000)

print(iter_time)
print(rec_time)


#Task 3
def outer_list():
    list_of_n = [25, 56, 91, 66, 6, 78, 76, 98, 54, 7, 27, 7, 21, 83, 58]

    def filter_sum(func):
        for item in list_of_n:
            if not func(item):
                list_of_n.remove(item)
        return sum(list_of_n)

    return filter_sum


def even(x):
    return not bool(x % 2)


def odd(x):
    return bool(x % 2)


filter_x = outer_list()
print(filter_x(even))
print(filter_x(odd))
