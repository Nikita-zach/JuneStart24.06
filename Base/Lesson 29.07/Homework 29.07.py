def data_in_line(line):
    users_data = line.split()
    amount = float(users_data[-2].strip("$"))
    categ = users_data[-1]
    name = users_data[1] + (" " + users_data[2] if "$" not in users_data[2] else "")
    return amount, categ, name


def format_two(diction):
    return {key: round(value, 2) for key, value in diction.items()}


def exp_by_cat(lines):
    by_cat = {}
    with open("hw_10_test.txt","r", encoding="UTF-8") as file:
        for line in file:
            amount, categ, _ = data_in_line(line)
            if categ in by_cat:
                by_cat[categ] += amount
            else:
                by_cat[categ] = amount


    return format_two(by_cat)


def exp_by_users(lines):
    by_user = {}
    with open("hw_10_test.txt","r", encoding="UTF-8") as file:
        for line in file:
            amount, _, name = data_in_line(line)
            if name in by_user:
                by_user[name] += amount
            else:
                by_user[name] = amount

    return format_two(by_user)


file = open("hw_10_test.txt", "r", encoding="UTF-8")


def exp_by_user(lines):
    user_exp = {}
    with open("hw_10_test.txt","r", encoding="UTF-8") as file:
        for line in file:
            amount, categ, name = data_in_line(line)
            if user_name == name:
                if categ in user_exp:
                    user_exp[categ] += amount
                else:
                    user_exp[categ] = amount


    return format_two(user_exp)


user_name = input("Enter name of a user>>>")
res = exp_by_cat(file)
res1 = exp_by_users(file)
res2 = exp_by_user(file)
print("\nExpenses by category:")
print(res)
print("\nExpenses by user:")
print(res1)
print(f"\n{user_name} spent money on: {res2}")
