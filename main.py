balance = 0
transactions = [
]
from tabulate import tabulate
def display_menu():
    print("\n--- Finance Tracker ---")
    print("1. Add income")
    print("2. Add expense")
    print("3. View balance")
    print("4. View transactions")
    print("5. Search a transaction")
    print("6. Exit")
def choice_select():
    while True:
        try:
            choice = int(input("Enter the number of your choice!"))
            match choice:
                case 1|2|3|4|5|6:
                    return choice
                case _:
                    print("Error: Number must be between 1 and 6.")
        except ValueError:
            print("Enter a valid number!")
def display_balance():
    print(f"Current balance: {balance}")
    input()
def deposit():
    category = input("What is the category of your deposit?")
    description = input("Small description regarding your deposit.")
    global balance
    transaction_amount = float(input("Enter the amount of your deposit."))
    balance = balance + transaction_amount
    print(f"You deposited: {transaction_amount}$")
    transaction = {
        "Category" : category,
        "Amount" : transaction_amount,
        "Description" : description
    }
    transactions.append(transaction)
def withdraw():
    category = input("What is the category of your withdraw?")
    description = input("Small description regarding your withdraw.")
    global balance
    transaction_amount = float(input("Enter the amount of your withdraw."))
    balance = balance - transaction_amount
    print(f"You withdrew: {transaction_amount}$")
    transaction = {
        "Category" : category,
        "Amount" : transaction_amount * -1,
        "Description" : description
    }
    transactions.append(transaction)
def display_transactions():
    if len(transactions) == 0:
        print("No transaction has occcured!")
        input()
    else:
        print(tabulate(transactions, headers="keys", tablefmt="grid"))
        input()
def search_transaction():
    if len(transactions) == 0:
        print("No transactions have occured!")
        input()
        return 
    search_term = input("What category do you want to search for?")
    search_item = input("Enter the item for searching.")
    check = False
    if search_term in ["Category","Amount","Description"]:
        match search_term:
            case "Category":
                for transaction in transactions:
                    if transaction["Category"] == search_item:
                        check = True
                        print(f"{transaction["Category"]}|{transaction["Amount"]}|{transaction["Description"]}")
            case "Amount":
                for transaction in transactions:
                                if transaction["Amount"] == float(search_item):
                                    check = True
                                    print(f"{transaction["Category"]}|{transaction["Amount"]}|{transaction["Description"]}")
            case "Description":
                for transaction in transactions:
                    if transaction["Description"] == search_item:
                        check = True
                        print(f"{transaction["Category"]}|{transaction["Amount"]}|{transaction["Description"]}")
        if check == False:
            print("No Matching record!")
        input()
display_menu()
choice = choice_select()
while choice != 6:
    if choice == 1:
        deposit()
    elif choice == 2:
        withdraw()
    elif choice == 3:
        display_balance()
    elif choice == 4:
        display_transactions()
    elif choice == 5:
        search_transaction()
    display_menu()
    choice = choice_select()



