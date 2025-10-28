import mysql.connector

# Connect to MySQL database
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root123",
    database="expense_db"
)

cur = conn.cursor()

# Add expense
def add_expense(date, category, amount, note):
    query = "INSERT INTO expenses (date, category, amount, note) VALUES (%s, %s, %s, %s)"
    cur.execute(query, (date, category, amount, note))
    conn.commit()
    print("Expense added successfully!")

# View all expenses
def view_expenses():
    cur.execute("SELECT * FROM expenses")
    for row in cur.fetchall():
        print(row)

# View total expense by category
def view_total_by_category():
    cur.execute("SELECT category, SUM(amount) FROM expenses GROUP BY category")
    results = cur.fetchall()
    print("\n--- Total Expenses by Category ---")
    for category, total in results:
        print(f"{category}: ₹{total:.2f}")

# Menu-driven program
while True:
    print("\n--- Expense Manager ---")
    print("1. Add Expense")
    print("2. View All Expenses")
    print("3. View Total by Category")
    print("4. Exit")
    choice = input("Enter choice: ")

    if choice == '1':
        date = input("Date (YYYY-MM-DD): ")
        category = input("Category: ")
        amount = float(input("Amount: "))
        note = input("Note: ")
        add_expense(date, category, amount, note)
    elif choice == '2':
        view_expenses()
    elif choice == '3':
        view_total_by_category()
    elif choice == '4':
        break
    else:
        print("Invalid choice!")

# Close connection
cur.close()
conn.close()
