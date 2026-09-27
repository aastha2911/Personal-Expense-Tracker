# Personal Expense Tracker

## Project Overview

Personal Expense Tracker is a Python-based application designed to help users record, manage, and analyse their daily expenses.

The project allows users to add expenses with their name, amount, and category. It also provides features for calculating total expenses, searching expenses by category, finding the highest and lowest expenses, and checking expenses against a monthly budget.

The project is divided into multiple Python modules.

---

## Features

The Personal Expense Tracker provides the following features:

1. Add Expense
   - Enter the name of an expense.
   - Enter the expense amount.
   - Enter the expense category.

2. View All Expenses
   - Displays all recorded expenses.
   - Shows the expense name, amount, and category.

3. Calculate Total Expense
   - Calculates the total amount spent.

4. Search Expense by Category
   - Allows the user to search for expenses belonging to a particular category.
   - Calculates the total amount spent in that category.

5. Find Highest Expense
   - Finds and displays the expense with the highest amount.

6. Find Lowest Expense
   - Finds and displays the expense with the lowest amount.

7. Set Budget and Check Balance
   - Allows the user to enter a monthly budget.
   - Calculates the total expenses.
   - Displays the remaining amount.
   - Indicates whether the user is within or over the budget.

8. Input Validation
   - Checks whether the menu choice is within the valid range.
   - Prevents zero or negative expense amounts.
   - Prevents empty expense names and categories.

---

## Technologies and Tools Used

- Python
- Visual Studio Code

### Python Concepts Used

- Variables
- Lists
- Input and Output
- Conditional Statements
- `for` loops
- `while` loops
- Functions
- Modules 
- String Operations
- Arithmetic Operations

---

## Project Structure

```text
Personal Expense Tracker/
│
├── main.py
├── expense_manager.py
├── analysis.py
├── budget_manager.py
└── validation.py