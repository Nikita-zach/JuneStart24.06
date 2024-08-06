# Task 1
text = input("Enter text>>>")
text = text.split()
res = {}
for item in text:
    res[item] = res.get(item, 0) + 1
print(res)

# Task 2
poor_translator={
    "i": "я",
    "love": "люблю",
    "python": "Пайтон"
}
res = ""
to_translate = input("Enter text to translate>>")
to_translate = to_translate.split()
for item in to_translate:
    res += poor_translator[item]+" " if item in to_translate else to_translate.pop(item)
print(res)

# Task 3
kontakty = {
    "mom": 727804123,
    "dad": 504123115
}
while True:
    question = input("Enter action(view numbers, add new number, delete number or stop): ")
    if question == "view numbers":
        for key, value in kontakty.items():
            print(key, value)
    elif question == "add new number":
        x = input("Enter name of a contact: ")
        y = input("Enter number: ")
        kontakty[x] = y
    elif question == "delete number":
        z = input("Enter contact you'd like to delete: ")
        del kontakty[z]
    elif question == "stop":
        break

# Task 4
valuty = {
    "dollar": 0.024,
    "euro": 0.022,
    "zloty": 0.095

}
curr, amount = input("Enter currency and amount of money you'd like to convert: ").split()
amount = int(amount)
print(f"Amount of currency after convertation: {amount * valuty[curr]}")