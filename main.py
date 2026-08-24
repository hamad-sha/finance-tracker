balance = 0
transactions = []
def display_menu():
    print("\n--- Finance Tracker ---")
    print("1. Add income")
    print("2. Add expense")
    print("3. View balance")
    print("4. View transactions")
    print("5. Exit")
def choice_select():
    while True:
        try:
            choice = int(input("Enter the number of your choice!"))
            match choice:
                case 1|2|3|4|5:
                    return choice
                case _:
                    print("Error: Number must be between 1 and 5.")
        except ValueError:
            print("Enter a valid number!")
def display_balance():
    print(f"Current balance: {balance}")
def transaction():
    global balance
    transaction_amount = float(input("Enter your income/expense."))
    balance = balance + transaction_amount
    if transaction_amount > 0:
        print(f"Your income inputted: {transaction_amount}")
    else:
        print(f"Your expense inputted: {transaction_amount}")
display_menu()
choice = choice_select()
while choice != 5:
    if choice in (1,2):
        transaction()
    elif choice == 3:
        display_balance()
    elif choice == 4:
        display_transactions()
    display_menu()
    choice = choice_select()



