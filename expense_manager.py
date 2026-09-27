# EXPENSE MANAGEMENT


from validation import valid_amount
from validation import valid_text


def add_expense(expenses, amounts, categories):

    print("\n========== ADD EXPENSE ==========")

    name = valid_text("Enter expense name: ")

    amount = valid_amount()

    category = valid_text("Enter category: ")

    expenses.append(name)
    amounts.append(amount)
    categories.append(category)

    print("Expense added successfully!")


def view_expenses(expenses, amounts, categories):

    print("\n========== ALL EXPENSES ==========")

    if len(expenses) == 0:

        print("No expenses have been added.")

    else:

        for i in range(len(expenses)):

            print("Expense:", expenses[i])
            print("Amount: ₹", amounts[i])
            print("Category:", categories[i])
            print("--------------------------------")