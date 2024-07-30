#Task 1
vop=str(input("У вас есть водительские права(yes or no):"))

if vop=="yes" or "no":
    if vop=="yes":
        print("Вы можете водить машину")
    if vop=="no":
        print("Вы не можете водить машину")

#Task 2

age=int(input("Введите свой возрост:"))
if age>=18:
    print("Вы можете получить водительские права")
else:
    print("Вы не отвичаете критериям для полученя водительских прав")

#Task 3

chislo=int(input("Введите число для проверки:"))
par=chislo%2
dod=chislo>0

if par==0 and bool(dod) is True:
    print("Введённое число положительное и парное.")
else:
    print("Введенное число не удовлетворяет критерии.")

#Task 4

krat=int(input("Введите число для проверки:"))
krat3=krat%3
niekrat5=krat%5

if bool(krat3==0) and bool(niekrat5>0) is True:
    print("Число подходит.")
else:
    print("Число не продходит.")