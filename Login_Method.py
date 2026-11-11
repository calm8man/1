#ابتدا نام کاربری و رمز صحیح را وارد کنید
correct_username=str(input("Enter your correct User_name:"))
correct_password=str(input("Enter your correct password:"))
max_attempts= 3

for attempt in range(max_attempts):
    user_name=input("Enter your User_name: ")
    password= input("Enter your password: ")
    if correct_username==user_name and correct_password==password:
        print("Login successful...")
        break
    else:
        print("Wrong user_name or password...")
else:
    print("Account locked...")