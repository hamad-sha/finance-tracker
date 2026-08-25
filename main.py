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
                case 1|2|3|4|5:
                    return choice
                case _:
                    print("Error: Number must be between 1 and 5.")
        except ValueError:
            print("Enter a valid number!")
def display_balance():
    print(f"Current balance: {balance}")
    input()
def transaction():
    category = input("What is the category of your payment?")
    description = input("Small description regarding your payment.")
    global balance
    transaction_amount = float(input("Enter your income/expense."))
    balance = balance + transaction_amount
    if transaction_amount > 0:
        print(f"Your income inputted: {transaction_amount}")
    else:
        print(f"Your expense inputted: {transaction_amount}")
    transaction = {
        "Category" : category,
        "Amount" : transaction_amount,
        "Description" : description
    }
    transactions.append(transaction)
def display_transactions():
    if len(transactions) == 0:
        print("No transaction has occcured!")
        input()
    else:
        counter = 0
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
    if choice in (1,2):
        transaction()
    elif choice == 3:
        display_balance()
    elif choice == 4:
        display_transactions()
    elif choice == 5:
        search_transaction()
    display_menu()
    choice = choice_select()



