

def show_balance():
    print(f"Your balance is ${balance:.2f}")

def deposit():
    amount=float(input("Enter an amount to be deposited: "))

    if amount<0:
        print("Thats not a valid amount  hththhtth")
    else:
        return amount

def withdraw():
    amount=float(input("Enter an amount tbe withdrawn: "))

    if amount>balance:
        print("Insufficient funds")
        return 0
    elif amount<0:
        print("Amountmust be greater than 0")
        return 0
    else:
        return amount
balance=0;
is_running=True;

while is_running:
    print("*********Banking program*********")
    print("1.Show Balance")      
    print("2.Deposit")
    print("3.Withdraw")
    print("4.Exit")

    choice=input("Enter your choice (1-4): ")

    if choice=='1':
        show_balance()
    elif choice=='2':
        balance+=deposit()
    elif choice=='3':
        balance-=withdraw()
    elif choice=='4':
        is_running=False
    else:
        print("That is an invalid choice input")
print("Thank you!Have a nice day.")
