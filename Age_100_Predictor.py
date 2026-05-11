# MAKING A USER INPUT THEIR NAME AND AGE, AND IN RESPONSE COMPUTER TELLS THEM WHEN THEY WILL TURN 100 YEARS OLD.
from datetime import date

user = input("Please give me your name: ")
print(f"Nice to meet you, {user}.")

today = date.today()

while True:
    try:
        age = int(input("Please can you tell me your age: "))
        if age < 0:
            print("Age cannot be negative. Please type your real age.")
            continue
        break
    except ValueError:
        print("Please enter a whole number.")

while True:
    try:
        month = int(input("Could you tell me what month you were born in? (1-12)"))
        if 1<=month<=12:
            break
        print("Month must be between 1 and 12.")
    except ValueError:
        print("Please enter a whole number.")
while True:
    try:
        day = int(input("Could you tell me what day you were born on? (1-31)"))
        if not 1<=day<=31:
            print("Day must be between 1 and 31.")
            continue
        if month in (4, 6, 9, 11) and day == 31:
            print("Sorry, these dates are invalid.")
            continue
        if month == 2 and day > 29:
            print("Sorry, these dates are invalid.")
            continue
        break
    except ValueError:
        print("Please enter a whole number.")
        continue

birth_year = (today.year - age)
if month > today.month or (month == today.month and day > today.day):
    birth_year = birth_year - 1
try:
    year_100 = date(birth_year + 100, month, day)
except ValueError:
        if month == 2 and day == 29:
            year_100 = date(birth_year + 100, 2, 28)
        else:
            print("This date is invalid.")
            exit()

print(f"By my calculations on {year_100} you will be 100 years old.")



