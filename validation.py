# INPUT VALIDATION


def valid_choice():

    choice = int(input("Enter your choice: "))

    while choice < 1 or choice > 8:

        print("Invalid choice. Please enter a number from 1 to 8.")

        choice = int(input("Enter your choice: "))

    return choice


def valid_amount():

    amount = float(input("Enter amount: "))

    while amount <= 0:

        print("Amount must be greater than 0.")

        amount = float(input("Enter amount: "))

    return amount


def valid_text(message):

    text = input(message)

    while text == "":

        print("This field cannot be empty.")

        text = input(message)

    return text