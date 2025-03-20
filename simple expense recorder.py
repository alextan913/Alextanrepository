def menu():
    print("\n--- Expense Tracker ---")
    print("1. Add Expense")
    print("2. View All Expenses")
    print("3. Calculate Total Spent")
    print("4. Exit")

def add_expense():
    while True:
        date = input("Enter date (YYYY-MM-DD): ")
        category = input("Enter category (example: Food, Transport): ")
        description = input("Enter a description: ")
        amount = input("Enter the amount of expense (RM): ")

        with open("expenses.txt", "a") as file:
            file.write(f"{date},{category},{description},{amount}\n")
    
        print("✅ Expense added successfully.")
        repeat = input("Do you want to add another expense? (Y/N): ")
        if repeat.lower() != 'y':
            break

def view_expenses():
    try:
        with open("expenses.txt", "r") as file:
            print("\n--- All Expenses ---")
            for line in file:
                date, category, description, amount = line.strip().split(",")
                print(f"{date} | {category} | {description} | RM{amount}")
    except FileNotFoundError:
        print("⚠️ No expenses recorded yet.")

def calculate_total():
    total = 0.0
    try:
        with open("expenses.txt", "r") as file:
            for line in file:
                parts = line.strip().split(",")
                if len(parts) == 4:
                    total += float(parts[3])
        print(f"\n💰 Total spent: RM{total:.2f}")
    except FileNotFoundError:
        print("⚠️ No expenses to calculate.")

# --- Main Program Loop ---
def main():
    while True:
        menu()
        choice = input("Choose an option (1-4): ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            calculate_total()
        elif choice == "4":
            print("👋 Exiting. Bye!")
            break
        else:
            print("❌ Invalid choice. Try again.")

main()
