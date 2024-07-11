#Task 8
x=[12,56,2,-4]
y=[item*2 for item in x]
print(x)
print(x+y)

#Task 9 очень похоже на то, что мы делали на уроке  :-)
salary=[]
MONTH=12
num=1
while len(salary)<MONTH:
    sal=int(input(f"Enter salary {num} month>>>"))
    salary.append(z)
    num+=1
print(salary)
print(sum(salary)/MONTH)

#Task 10
matrix=[[1, 2, 3, 4],[5, 6, 7, 8],[9, 10, 11, 12],[13, 14, 15, 16]]
n=0
for item in matrix:
    print(f"{matrix[n]}={sum(matrix[n])}")
    n+=1

#Task 11
spis=[1,3,4,5,6]
spis1=spis[::-1]
print(spis1)

#Task 12
for num in range(2, 101):
    prost = True
    for i in range(2, num):
        if num % i == 0:
            prost = False
            break
    if prost:
        print(num)

#Task 13
prov = True
while prov:
    shyr = int(input("Enter width of a figure:"))
    if shyr%2!=0:
        prov=False
werh=shyr
niz=3
space=0
for z in range(shyr):
    if z<shyr/2:
        print(" "*space+"*" * werh)
        space+=1
        werh -= 2
    elif z<(shyr/2+1):
        space -=2
        print(" " * space + "*" * niz)
        niz += 2
    else:
        space = (shyr - z)-1
        print(" " * space + "*" * niz)
        niz += 2