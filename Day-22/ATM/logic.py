data = {
    123456: {'name': 'prasanna', 'pin': '1234', 'balance': 50000, 'history': []},
    234567: {'name': 'samardhh', 'pin': '2345', 'balance': 70000, 'history': []},
    345678: {'name': 'sai', 'pin': '3456', 'balance': 10000, 'history': []}
}

def login():
    global acc_num

    acc_num = int(input("Enter the account number: "))
    pin = input("Enter the pin: ")

    if acc_num in data and data[acc_num]['pin'] == pin:
        print("Login successful")
        return True
    else:
        print("Invalid login")
        return False


def menu():
    print(f"\nWelcome to the ATM, {data[acc_num]['name']}")
    print("[c] Check balance")
    print("[d] Deposit")
    print("[w] Withdraw")
    print("[v] View transaction")
    print("[e] Exit")


def checkbalance():
    print(f"\nHello {data[acc_num]['name']},")
    print("Current balance:", data[acc_num]["balance"])


def deposite():
    amount = int(input("Enter the amount to deposit: "))

    if amount > 0:
        data[acc_num]["balance"] += amount
        data[acc_num]['history'].append(f"{amount} is deposited")
        print(f"{amount} is deposited successfully")
        checkbalance()
    else:
        print("Enter a valid amount")


def withdraw():
    amount = int(input("Enter the amount to withdraw: "))

    if amount <= 0:
        print("Enter a valid amount")

    elif data[acc_num]["balance"] >= amount:
        data[acc_num]["balance"] -= amount
        data[acc_num]['history'].append(f"{amount} is withdrawn")
        print(f"{amount} is withdrawn successfully")
        checkbalance()

    else:
        print("Insufficient balance")


def viewtransactions():
    if data[acc_num]['history']:
        print("\n==== Transaction History ====")

        for i in data[acc_num]['history']:
            print(i)

        print("==== End of Transaction History ====")

    else:
        print("No transaction history")


# Main program

if login():

    while True:
        menu()

        choice = input("Enter your choice: ").lower()

        if choice == 'c':
            checkbalance()

        elif choice == 'd':
            deposite()

        elif choice == 'w':
            withdraw()

        elif choice == 'v':
            viewtransactions()

        elif choice == 'e':
            print("Thank you for using the ATM")
            break

        else:
            print("Invalid choice")