salary=[]
MONTH=12
while len(salary)<MONTH:
    x=int(input("Enter month salary>>>"))
    salary.append(x)
print(f"Min salary: {min(salary)}")
print(f"Min salary: {max(salary)}")
print(f"Min salary: {sum(salary)/len(salary)}")
print(f"Min salary: {salary.index(min(salary))}")
print(f"Min salary: {salary.index(max(salary))}")