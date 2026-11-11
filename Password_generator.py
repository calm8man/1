import random

#ابتدا کاراکتر های حروف بزرگ و کوچک و اعداد را ایجاد میکنیم

#letters=""
#for i in range(ord("a"),ord("z")+1):
#   letters+=chr(i)
#print(letters)
letters="abcdefghijklmnopqrstuvwxyz"

#Letters=""
#for i in range(ord("A"),ord("Z")+1):
    #Letters+=chr(i)
#print(Letters)
Letters="ABCDEFGHIJKLMNOPQRSTUVWXYZ"

#numbers=""
#for i in range(ord("0"),ord("9")+1):
    #numbers+=chr(i)
#print(numbers)
numbers="0123456789"

symbols="@#$%_*^&"

all_character=letters+Letters+numbers+symbols
#print(all_character)

# اینجا تعداد کاراکتر های رمز مورد نظرتون را وارد میکنید. برای مثال: 8 کاراکتر
length=int(input("Enter password length: "))

password=""
for i in range(length):
    password+=random.choice(all_character)
print(f"Your password is :{password}")