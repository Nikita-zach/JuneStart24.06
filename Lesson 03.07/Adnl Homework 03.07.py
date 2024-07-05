#Task 1

password=str(input("Введите пароль(подсказка 1*4):"))
res="Доступ запрещен"
if password=="1111":
    res="Доступ разрещен"
print(res)

#Task 2

money=float(input("Введите сумму покупок:"))
if money>=1000:
    money=money*0.9
print(f"Сумма покупок:{money} гривен")

#Task 3

month=int(input("Введите месяц по счету(1-12):"))
if month==2:
    print("В данном месяце 28(29,если год высокосный) дней")
elif 1<=month<=7 and not month==2:
    if month%2:
        print("В данном месяце 31 день")
    else:
        print("В данном месяце 30 дней")
elif 8 <= month <=  12 and not month == 2:
    if month%2:
        print("В данном месяце 30 дней")
    else:
       print("В данном месяце 31 день")
else:
    print("Введён неверный номер месяца")

#Task 4

rate=int(input("Введите свою оценку(1-5):"))


if rate%2 and not rate==3:
    result = 'Отлично' if rate>3 else 'Ужасно'
    print(result)
elif not rate%2:
    result = 'Хорошо' if rate > 3 else 'Плохо'
    print(result)
else:
    print("Удовлетворительно")

#Task 5

rost=float(input("Введите свой рост(м):"))
ves=float(input("Введите свой вес(кг):"))
indeks=ves/(rost**2)
if indeks<=25:
    resul="Недостаточный вес" if indeks<18.5 else "Нормальный вес"
    print(resul)
elif indeks>25:
    resul="Избыточный вес" if indeks<30 else "Ожирение"
    print(resul)
