#Task 1
def procent_ot_zp(a, b):
    return a - (a * (b / 100))
money = int(input("Enter your month salary>>>"))
proc = int(input("Enter your income tax percentage>>>"))
print(procent_ot_zp(money, proc))

#Task 2
import random
import string
def password(dlina, znaki):
    spec = string.punctuation
    parol = [str(random.choice([random.randint(1, 10), random.choice(spec)]) if znaki == True
                 else random.randint(1, 10)) for _ in range(dlina)]
    res = "".join(parol)
    return res
dlina_pass = int(input("Enter preferred length of generated password>>>"))
spec_zn = input("Does special symbols required?(yes or no)")
znaki_bool = True if spec_zn.lower() == "yes" else False
print(password(dlina_pass, znaki_bool))


#Task 3
spis = {}
for i in range(999,99,-1):
    for x in range(i,99,-1):
        chislo = str(i * x)
        if chislo[:len(chislo)//2] == chislo[-1:len(chislo)//2:-1]:
            spis[chislo] = i, x
        else:
            pass
max_palindr = max(spis)
print(f"The biggest palindrome is {max_palindr} = {spis[max_palindr][0]} * {spis[max_palindr][1]}")

#Task 4

def arif_prog(spis):
    razn = spis[1] - spis[0]
    for i in range(len(spis) - 1):
        if spis[i + 1] - spis[i] != razn:
            return False
    return True


def geom_prog(spis):
    razn_del = spis[1] / spis[0]
    for i in range(len(spis)-1):
        if spis[i + 1] / spis[i] != razn_del:
            return False
    return True


spisok = (input("Enter several number>>>")).split()
numbers = [int(digit) for digit in spisok if digit.isdigit()]
if arif_prog(numbers):
    print(numbers[-1] + numbers[1] - numbers[0])
elif geom_prog(numbers):
    print(int(numbers[-1] * numbers[1] / numbers[0]))

#Task 5
import num2words
how_much = float(input("Enter amount of money>>>"))
how_much *= 100
dollars = how_much // 100
cents = how_much % 100
cent = "cent" if cents % 10 == 1 else "cents"
dollar = "dollar" if dollars % 10 == 1 else "dollars"
print(f"{num2words.num2words(dollars)} {dollar} and {num2words.num2words(cents)} {cent}")