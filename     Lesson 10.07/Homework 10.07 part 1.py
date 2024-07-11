#Task 1
for x in range(1,100):
    if x%7==0:
       print(x)

#Task 2
summa=0
count=0
for y in range(1,100):
    if y%2!=0:
        count+=1
        summa+=y
print(summa)
print(count)

#Task 3
z=list(range(1,201))
while len(z)>0:
    print(z.pop(0),z.pop(0),z.pop(0),z.pop(0),z.pop(0))

#Task 4
cifra=1
fractal=1
n=int(input("Enter your number>>>"))
for c in range(n):
    fractal*=cifra
    cifra+=1
print(f"Fractal to number equal:{fractal}")

#Task 5
MNOZH=5
chisl=1
for d in range(10):
    print(f"{chisl}x{MNOZH}={chisl*MNOZH}")
    chisl+=1

#Task 6
vys,shyr=map(int,input("Enter parameters to rectangle>>>").split())
print("*"*shyr)
for t in range(vys-2):
    print("*"+" "*(shyr-2)+"*")
print("*"*shyr)

#Task 7
spis=[0, 5, 2, 4, 7, 1, 3, 19]
niepar_spis = [item for item in spis if item % 2 != 0]
print(sum(niepar_spis))
