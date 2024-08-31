menu = """

[D] Deposit
[W] Withdrawal
[S] Statement
[L] Leave

==> """

balance = 0
withdrawal_limit = 500
statement = ""
amount_of_withdrawals = 0
MAX_WITHDRAWAL = 3

while True:

    choice = str(input(menu)).upper

    if choice == "D":
        print("Deposit")

    elif choice == "W":
        print("Withdrawal")
    
    elif choice == "S":
        print("Statement")

    elif choice == "L":
        break

    else:
        print("Invalid input. Please, type a valid option.")