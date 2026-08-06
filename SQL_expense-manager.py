import sqlite3

class ExpenseTracker:
    def __init__(self, db_name="expenses.db"):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS expenses (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                category TEXT,
                amount REAL,
                description TEXT
            )
        ''')
        self.conn.commit()

    def add_expense(self, category, amount, description):
        self.cursor.execute(
            "INSERT INTO expenses (category, amount, description) VALUES (?, ?, ?)",
            (category, amount, description)
        )
        self.conn.commit()
        print("Expense added successfully.")

    def get_summary(self):
        self.cursor.execute("SELECT category, SUM(amount) FROM expenses GROUP BY category")
        return self.cursor.fetchall()

    def close(self):
        self.conn.close()

# Usage
# tracker = ExpenseTracker()
# tracker.add_expense("Food", 250.50, "Lunch")
# print(tracker.get_summary())
# tracker.close()
