#Task 1
ticket=input("Enter your ticket numbers(only 4 of them):")
numbers=list(map(int,ticket))
if numbers[0] + numbers[1] == numbers[2] + numbers[3]:
    print("You've got a lucky ticket.YAY!!!")
else:
    print("Beter luck next time.:-(")

#Task 2
num=input("Enter 6-figure number:")
res="This is a palindrome" if num==num[::-1] else "This is not palindrome"
print(res)

#Task 3
R=16
x,y = int(input("Enter x:")),int(input("Enter y:"))
PROV=x**2+y**2
if PROV<R:
    print("Point is in a circle")
else:
    print("Point isn't in a circle")