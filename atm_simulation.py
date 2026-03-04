# Simple ATM Simulation

balance = 10000

while True:
    print("\n1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        print("Your balance is:", balance)

    elif choice == "2":
        amount = float(input("Enter deposit amount: "))
        balance += amount
        print("Amount deposited successfully")

    elif choice == "3":
        amount = float(input("Enter withdraw amount: "))
        if amount <= balance:
            balance -= amount
            print("Amount withdrawn successfully")
        else:
            print("Insufficient balance")

    elif choice == "4":
        print("Thank you for using ATM")
        break

    else:
        print("Invalid choice")
