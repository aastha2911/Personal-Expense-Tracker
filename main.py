# PERSONAL EXPENSE TRACKER
# MAIN PROGRAM

from expense_manager import add_expense
from expense_manager import view_expenses

from analysis import calculate_total
from analysis import search_category
from analysis import highest_expense
from analysis import lowest_expense

from budget_manager import budget_check

from validation import valid_choice
from validation import valid_amount
from validation import valid_text


expenses = []
amounts = []
categories = []

choice = 0

while choice != 8:

    print("\n================================")
    print("       PERSONAL EXPENSE TRACKER")
    print("================================")
    print("1. Add Expense")
    print("2. View All Expenses")
    print("3. Calculate Total Expense")
    print("4. Search Expense by Category")
    print("5. Find Highest Expense")
    print("6. Find Lowest Expense")
    print("7. Set Budget and Check Balance")
    print("8. Exit")
    print("================================")

    choice = valid_choice()

    if choice == 1:

        add_expense(expenses, amounts, categories)

    elif choice == 2:

        view_expenses(expenses, amounts, categories)

    elif choice == 3:

        calculate_total(amounts)

    elif choice == 4:

        search_category(expenses, amounts, categories)

    elif choice == 5:

        highest_expense(expenses, amounts, categories)

    elif choice == 6:

        lowest_expense(expenses, amounts, categories)

    elif choice == 7:

        budget_check(amounts)

    elif choice == 8:

        print("\nThank you for using Personal Expense Tracker!")
        print("Goodbye!")