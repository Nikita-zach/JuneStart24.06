#Task 1

x=int(input("Number>>>"))
if x<0:
    print(x)


#Task 2

prov=int(input("Введите цело число:"))
obr=prov<20
print(obr)

#Task 3
cel=int(input("Введите число:"))
da=bool(cel==0)
print(da)

#Task 4

pnp=int(input("Введите число:"))
pn=pnp%2
if pn==0:
    print("Число являеться парным")
else:
    print("Число являеться непарным")

#Task 5

def kakoe(g,h,j):
    return max(g,h,j)

adyn=float(input("Введите число:"))
dwa=float(input("Введите число:"))
tryy=float(input("Введите число:"))

maxchislo=kakoe(adyn,dwa,tryy)

print(f"Самое большое число:{maxchislo}")