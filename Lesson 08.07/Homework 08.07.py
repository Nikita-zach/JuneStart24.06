#Task 1
ticket=input("Enter your ticket numbers(only 4 of them):")
numbers=list(map(int,ticket))
if numbers[0] + numbers[1] == numbers[2] + numbers[3]:
    print("You've got a lucky ticket.YAY!!!")
else:
    print("Beter luck next time.:-(")

#Task 2
num=input("Enter 6-figure number:")
palindrome=list(map(int,num))
pal1=polindrome[0:3]
pal2=polindrome[-1:-4:-1]
res="This is a palindrome" if pal1==pal2 else "This is not palindrome"
print(res)

#Task 3
RAD = 4
x,y = int(input("Enter x:")),int(input("Enter y:"))
result = "Point is in a circle" if x<=RAD and y<=RAD else "Point isn't in a circle"
print(result)