import bank_functions as fc

menu = """

[D] Deposit
[W] Withdrawal
[S] Statement
[L] Leave

==> """

balance = 0
withdraw_limit = 500
statement = ""
amount_of_withdraws = 0
MAX_WITHDRAW = 3

while True:

    choice = str(input(menu)).upper()

    if choice == "D":
        print("\nDeposit\n")
        deposit_value = float(input("Type how much you want to deposit\n\n==> "))
        if deposit_value <= 0:
            print("Invalid input. You can't deposit a negative amount of money.")
            continue
        statement = "\n".join((statement, f"Deposit\nR$ {balance:.2f} + R$ {deposit_value:.2f} = R$ {balance + deposit_value:.2f}"))
        balance = fc.deposit(balance=balance, deposit_value=deposit_value)

    elif choice == "W":
        print("Withdraw")
        if amount_of_withdraws >= MAX_WITHDRAW:
            print("Max withdraw limit reached. Please try again tomorrow.")
            continue
        withdraw_value = float(input("Type how much you wish to withdraw\n\n==> "))
        if withdraw_value < 0:
            print("You can't withdraw a negative amount of money. Please try again.")
            continue
        elif withdraw_value > withdraw_limit:
            print(f"You can't withdraw more than {withdraw_limit:.2f}. Please try again.")
            continue
        elif withdraw_value > balance:
            print("Not enough balance. Please try again.")
            continue
        amount_of_withdraws += 1
        statement = "\n".join((statement, f"Withdraw\nR$ {balance:.2f} - R$ {withdraw_value:.2f} = R$ {balance - withdraw_value:.2f}"))
        balance = fc.withdraw(balance=balance, withdraw_value=withdraw_value)
    
    elif choice == "S":
        print("Statement")
        print(f"{statement}\nCurrent balance: R$ {balance:.2f}")

    elif choice == "L":
        print("Thanks and come again!")
        break

    else:
        print("Invalid input. Please, type a valid option.")
