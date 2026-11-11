def show_menu():
    print("1. Show Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")


def deposit(balance, amount):
    if amount <= 0:
        print("Amount must be positive...")
        return balance
    print("Deposit successful...")
    return balance + amount


def withdraw(balance, amount):
    if amount <= 0:
        print("Amount must be positive...")
    elif amount > balance:
        print("Not enough balance...")
    else:
        print("Withdraw successful...")
        return balance - amount
    return balance


def get_int(message):
    try:
        return int(input(message))
    except ValueError:
        print("Please enter a valid number...")
        return None


correct_password = "123"
balance = 2000000

if input("Enter your password: ") == correct_password:
    while True:
        show_menu()
        cmd = get_int("Enter your cmd number: ")
        if cmd == 1:
            print(f"Your balance is {balance}")
        elif cmd == 2:
            amount = get_int("Enter deposit amount: ")
            if amount is not None:
                balance = deposit(balance, amount)
        elif cmd == 3:
            amount = get_int("Enter withdraw amount: ")
            if amount is not None:
                balance = withdraw(balance, amount)
        elif cmd == 4:
            break
        else:
            print("Invalid command...")
else:
    print("Wrong password...")