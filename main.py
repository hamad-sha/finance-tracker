Balance = 0
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

display_menu()

