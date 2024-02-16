import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt
from collections import defaultdict

class ExpenseTracker:
    def __init__(self, root):
        self.root = root
        self.root.title("Expense Tracker")
        self.expenses = defaultdict(float)

        self.label = tk.Label(root, text="Enter Expense:")
        self.label.grid(row=0, column=0)

        self.expense_entry = tk.Entry(root)
        self.expense_entry.grid(row=0, column=1)

        self.amount_label = tk.Label(root, text="Enter Amount:")
        self.amount_label.grid(row=1, column=0)

        self.amount_entry = tk.Entry(root)
        self.amount_entry.grid(row=1, column=1)

        self.category_label = tk.Label(root, text="Enter Category:")
        self.category_label.grid(row=2, column=0)

        self.category_entry = tk.Entry(root)
        self.category_entry.grid(row=2, column=1)

        self.submit_button = tk.Button(root, text="Submit", command=self.add_expense)
        self.submit_button.grid(row=3, columnspan=2)

        self.view_button = tk.Button(root, text="View Expenses", command=self.view_expenses)
        self.view_button.grid(row=4, columnspan=2)

    def add_expense(self):
        expense = self.expense_entry.get()
        amount = float(self.amount_entry.get())
        category = self.category_entry.get()

        self.expenses[category] += amount
        messagebox.showinfo("Expense Added", f"Expense '{expense}' of ${amount} added to category '{category}'.")

        self.expense_entry.delete(0, tk.END)
        self.amount_entry.delete(0, tk.END)
        self.category_entry.delete(0, tk.END)

    def view_expenses(self):
        if not self.expenses:
            messagebox.showinfo("No Expenses", "No expenses added yet.")
            return

        categories = list(self.expenses.keys())
        amounts = list(self.expenses.values())

        plt.bar(categories, amounts, color='skyblue')
        plt.xlabel('Categories')
        plt.ylabel('Amount ($)')
        plt.title('Expense Tracker')
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()

if __name__ == "__main__":
    root = tk.Tk()
    app = ExpenseTracker(root)
    root.mainloop()
      
