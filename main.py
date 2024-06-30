#Task 1

name=input("Напишите свое имя:")
print(f"Здравствуйте, {name}!")



#Task 2

a=input("Введите первую цифру:")
b=input("Введите вторую цифру:")
c=input("Введите третью цифру:")
d=input("Введите четвертую цифру:")
e=input("Введите пятую цифру:")

a=int(a)
b=int(b)
c=int(c)
d=int(d)
e=int(e)

f=(max(a,b,c,d,e))
g=(min(a,b,c,d,e))
h=(a+b+c+d+e)
h=float(h)
print(f"Максимальное значение: {f}")
print(f"Минимальное значение: {g}")
print(f"Среднее арифметическое значение: {h/5}")



#Task 3

x=input("Введите первое число:")
y=input("Введите второе число:")

x=int(x)
y=int(y)

print(f"Сложение: {x+y}")
print(f"Вычитание: {x-y}")
print(f"Умножение: {x*y}")
print(f"Деление: {x/y}")
print(f"Деление без остатка: {x//y}")



#Task 4

r=input("Введите радиус окружности:")

r=int(r)
print(f"Диаметр окуржности: {r*2}см")
print(f"Площадь окружности: {3.14*r**2}см2")
print(f"Длина окружности: {6.28*r}см")



#Task 5

inv=input("Bведите сумму инвестиции:")
n=input("Введите срок инвистиции:")
inv=int(inv)
n=int(n)
prc=0.1
prc=float(prc)
result=inv*(1+prc)**n
result=float(result)

print(f"Конечная сумма инвистициий по заверешнию заданного срока: {result}")



#Task 6

dol=input("Введите сумму в долларах:")
dol=float(dol)

kurs=40.46
print(f"Cумма после конвретации {dol*kurs} долларов")
