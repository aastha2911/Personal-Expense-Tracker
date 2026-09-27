# BUDGET MANAGEMENT

from validation import valid_amount


def budget_check(amounts):

    print("\n========== BUDGET ==========")

    budget = valid_amount()

    total = 0

    for amount in amounts:
        total = total + amount

    remaining = budget - total

    print("Monthly Budget: ₹", budget)
    print("Total Expense: ₹", total)
    print("Remaining Amount: ₹", remaining)

    if remaining > 0:
        print("You are within your budget.")

    elif remaining == 0:
        print("You have used your entire budget.")

    else:
        print("You have exceeded your budget.")