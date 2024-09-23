#Task 1
import re

string = "rkBBBbbbr q12ef RbbbBbbr123 plkjrbR"
rbr_pattern = r"[Rr]{1}[Bb]+[Rr]{1}"
result = re.findall(rbr_pattern, string)
print(result)

#Task 2

card_number = "9999-9999-9999-9999-9999"
number_pattern = r"^\d{4}-\d{4}-\d{4}-\d{4}(-\d{4})?"
result = re.match(number_pattern, card_number)
if result:
    print("Good Job :-)")
else:
    print("Try Again :-(")

#Task 3

e_mail = "VasyaPupkin_2002@gmail.com"
mail_pattern = r"^[A-Za-z0-9](?:[A-Za-z0-9._%+-]*)@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$"

result = re.match(mail_pattern, e_mail)
if result:
    print("Good Job :-)")
else:
    print("Try Again :-(")



#Task 4

login = "Krutoj330"
login_pattern = r"^[A-Za-z0-9]{2,10}$"
check = re.fullmatch(login_pattern, login)
if check:
    print("Good Job :-)")
else:
    print("Try Again :-(")

