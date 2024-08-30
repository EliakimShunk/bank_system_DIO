menu = """

[D] Deposit
[W] Withdrawal
[S] Statement
[L] Leave

==> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

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