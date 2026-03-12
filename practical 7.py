def addition(a, b):
    return a + b

def subtraction(a, b):
    return a - b

def multiplication(a, b):
    return a * b

def division(a, b):
    return a / b

def modulus(a, b):
    return a % b

while True:
    print("\n--- CALCULATOR MENU ---")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Modulus")
    print("6. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 6:
        print("Exiting program")
        break

    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))

    if choice == 1:
        print("Result:", addition(a, b))
    elif choice == 2:
        print("Result:", subtraction(a, b))
    elif choice == 3:
        print("Result:", multiplication(a, b))
    elif choice == 4:
        print("Result:", division(a, b))
    elif choice == 5:
        print("Result:", modulus(a, b))
    else:
        print("Invalid Choice")
balance = 0

def display_balance():
    print("Current Balance:", balance)

def deposit(amount):
    global balance
    balance = balance + amount
    print("Amount Deposited Successfully")

def withdraw(amount):
    global balance
    if amount > balance:
        print("Insufficient Balance")
    else:
        balance = balance - amount
        print("Withdrawal Successful")

while True:
    print("\n--- BANK MENU ---")
    print("1. Display Balance")
    print("2. Deposit Amount")
    print("3. Withdraw Amount")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        display_balance()

    elif choice == 2:
        amount = int(input("Enter amount to deposit: "))
        deposit(amount)

    elif choice == 3:
        amount = int(input("Enter amount to withdraw: "))
        withdraw(amount)

    elif choice == 4:
        print("Thank you!")
        break

    else:
        print("Invalid choice")