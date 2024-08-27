#Task 2
def geom_prog(start, step):
    current = start
    while True:
        yield current
        current *= step


x = geom_prog(4, 2)
for i in range(5):
    print(next(x))


#Task 3
def own_range(start, end=None, step=1):
    if end is None:
        start, end = 0, start
    if step == 0:
        raise ValueError("Step cannot be zero")

    curr = start
    if step > 0:
        while curr < end:
            yield curr
            curr += step
    if step < 0:
        while curr > end:
            yield curr
            curr += step


for i in own_range(12, 4, -2):
    print(i)


#Task 4

def simple_numbers(n):
    for num in range(2, n):
        prost = True
        for i in range(2, num):
            if num % i == 0:
                prost = False
                break
        if prost:
            yield num


z = simple_numbers(49)
for _ in range(10):
    print(next(z))

#Task 5

import datetime


def date_generator(start_date, end_date):
    current_date = start_date
    while current_date <= end_date:
        yield current_date
        current_date += datetime.timedelta(days=1)


first = datetime.datetime(2023, 8, 1)
last = datetime.datetime(2024, 3, 1)

for date in date_generator(first, last):
    print(date.strftime("%Y-%m-%d"))
