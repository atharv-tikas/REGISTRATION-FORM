balance = 5000
pin = "1234"

entered_pin = input("Enter your ATM PIN: ")

if entered_pin == pin:
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")

    choice = input("Choose an option: ")
    if choice == "1":
        print("Balance:", balance)

    elif choice == "2":
        amount = float(input("Enter deposit amount: "))
        if amount > 0:
            balance += amount
            print("New balance:", balance)
        else:
            print("Invalid amount")

    elif choice == "3":
        amount = float(input("Enter withdrawal amount: "))
        if 0 < amount <= balance:
            balance -= amount
            print("Please collect your cash.")
            print("Remaining balance:", balance)
        else:
            print("Invalid amount or insufficient balance")

    else:
        print("Invalid choice")
else:
    print("Incorrect PIN")
