#Task 1
def unique(spis):
    return True if len(spis) == len(set(spis)) else False
res = unique(input("Enter text>>>").split())
print(res)

#Task 2
listok = input("Enter text>> ").split()
print(f"Number of unique items: {len(set(listok))}")

#Task 3
slown = {}
i=1
while (klucz := input("Enter item to add : ")) != "":
    slown[i] = klucz
    i += 1
znacz = list(slown.values())
print(len(set(znacz))>1)

#Task 4
ludi = {
    "Misha": {"Sergej", "Aleksej","Nikita"},
    "Pasha": {"Vova", "Sergej"},
    "Vlad": {"Nikita", "Dmitrij"},
    "Kiril": {"Sergej", "Vova", "Dmitrij"}
}
kogo = input("Enter 2 names to find common friends : ").title().split()
friendship = ludi[kogo[0]] & ludi[kogo[1]]
print(*friendship)

#Task 5
text_1 = set(input("Enter first text>>>").split())
text_2 = set(input("Enter second text>>>").split())
smierh = list(text_1 & text_2)
print(max(smierh, key = len))