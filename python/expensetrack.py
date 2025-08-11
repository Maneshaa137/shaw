import csv
from datetime import datetime

FILE_NAME = "expenses.csv"

# Initialize CSV with headers if not present
def init_file():
    try:
        with open(FILE_NAME, 'x', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Date", "Category", "Amount", "Description"])
    except FileExistsError:
        pass

# Add new expense
def add_expense():
    category = input("Enter category (Food, Transport, Bills, etc.): ")
    amount = float(input("Enter amount: "))
    description = input("Enter description: ")
    date = datetime.now().strftime("%Y-%m-%d")
    
    with open(FILE_NAME, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([date, category, amount, description])
    
    print("✅ Expense added successfully!\n")

# View all expenses
def view_expenses():
    with open(FILE_NAME, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)

# Delete all expenses
def clear_expenses():
    confirm = input("⚠️ Are you sure you want to delete all expenses? (y/n): ")
    if confirm.lower() == 'y':
        with open(FILE_NAME, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Date", "Category", "Amount", "Description"])
        print("🗑️ All expenses deleted!\n")

# Main menu
def main():
    init_file()
    while True:
        print("\n📌 Expense Tracker")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Clear Expenses")
        print("4. Exit")
        choice = input("Choose an option: ")
        
        if choice == '1':
            add_expense()
        elif choice == '2':
            view_expenses()
        elif choice == '3':
            clear_expenses()
        elif choice == '4':
            print("👋 Exiting... Goodbye!")
            break
        else:
            print("❌ Invalid option. Try again.")

if __name__ == "__main__":
    main()
