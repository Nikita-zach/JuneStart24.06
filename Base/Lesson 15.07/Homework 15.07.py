#Task 1
text=input("Enter string>>>")
print(text.count("b"))

#Task 2
#name=input("Enter your name>>>")
#res=""
#x=1
#for item in name:
#    if not item.isupper() and item==name[0]:
#        res+="First letter must be in upper case.\n"
#    elif not item.islower() and item!=name[0] and x==1:
#        res+="All letters except first must be in lower case\n"
#        x+=1
#    elif item.isdigit() and x==1 or x==2:
#        res+="Digits are not allowed\n"
#        x+=2
#print(res)
#if not len(res):
#    print("Have a nice day")

name=input("Enter your name>>>")
x=[item for item in name]
y=True
for item in x:
    if item.isdigit():
        print("You've entered a digit, please try again.")
        y=False
if not name.istitle():
    print("Please follow the rules of a title")
elif name.istitle() and y==True:
    print("Thank you, have a nice day")

#Task 3
kod=input("Enter string>>>")
kod_da=[]
for item in kod:
    kod_da.append(ord(item))
print(sum(kod_da))

or    #Я не понял условия таска:-(

kod1=input("Enter string>>>")
kod_da1=kod1.split()
print(len(kod_da1))

#Task 4
import math
n=2
for i in range(10):
    print(f"Pi = {math.pi:.{n}f}")
    n+=1

#Task 5
slowo=input("Enter some words>>>")
max_slowo=slowo.split()
dlina=[len(item) for item in max_slowo]
print(max_slowo[dlina.index(max(dlina))])

#Task 6
rep_words=input("Enter repeated text>>>")
for i in range(1,len(rep_words) // 2 + 1):
    candidate=rep_words[:i]
    if candidate*(len(rep_words)//len(candidate))==rep_words:
        word=candidate
        break

print(f"Your word is - {word}")

# Task 7

x = "Да<div id=rcnt>, у меня есть 100 доларов </div id=rcnt>"
for i in range(2):
    ind1, ind2 = x.find("<"), x.find(">")
    x = x[:ind1] + x[ind2 + 1:]
print(x)

# или

x1 = "<div id=rcnt>Да, у меня есть 100 долларов</div id=rcnt>"

ind3 = x.find(">")
ind4 = x.find("</")
x2 = x[ind3 + 1:ind4]
print(x2)