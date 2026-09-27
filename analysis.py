# EXPENSE ANALYSIS


def calculate_total(amounts):

    total = 0

    for amount in amounts:
        total = total + amount

    print("\nTotal Expense = ₹", total)


def search_category(expenses, amounts, categories):

    if len(expenses) == 0:

        print("No expenses have been added.")

    else:

        search = input("Enter category to search: ")

        found = 0
        category_total = 0

        print("\n===== EXPENSES IN", search, "=====")

        for i in range(len(expenses)):

            if categories[i].lower() == search.lower():

                print("Expense:", expenses[i])
                print("Amount: ₹", amounts[i])
                print("--------------------------------")

                category_total = category_total + amounts[i]
                found = found + 1

        if found == 0:

            print("No expenses found in this category.")

        else:

            print("Total spent in", search, "= ₹", category_total)


def highest_expense(expenses, amounts, categories):

    if len(amounts) == 0:

        print("No expenses have been added.")

    else:

        highest = amounts[0]
        highest_index = 0

        for i in range(len(amounts)):

            if amounts[i] > highest:

                highest = amounts[i]
                highest_index = i

        print("\n===== HIGHEST EXPENSE =====")
        print("Expense:", expenses[highest_index])
        print("Amount: ₹", amounts[highest_index])
        print("Category:", categories[highest_index])


def lowest_expense(expenses, amounts, categories):

    if len(amounts) == 0:

        print("No expenses have been added.")

    else:

        lowest = amounts[0]
        lowest_index = 0

        for i in range(len(amounts)):

            if amounts[i] < lowest:

                lowest = amounts[i]
                lowest_index = i

        print("\n===== LOWEST EXPENSE =====")
        print("Expense:", expenses[lowest_index])
        print("Amount: ₹", amounts[lowest_index])
        print("Category:", categories[lowest_index])