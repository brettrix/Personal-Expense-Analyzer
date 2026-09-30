#Author: Brett Rix
#Create a Python program that analyzes a series of personal expenses.

#Repeatedly ask the user to enter expenses until they enter a 0 to indicate they are finished
#entering expenses. Ensure that the expenses that the user inputs are valid (i.e. not negative.)
#(Note: The easiest way to store expenses will be to use a Python list. We have not covered in
#class how to add things to a list, so you will need to figure out how to do that.)
expense_list = []
given_expense = None
while given_expense != 0:
    given_expense = float(input("Enter an expense (or 0 to finish): "))
    if given_expense < 0:
        print("Please enter a valid expense (not negative).")
    elif given_expense > 0:
        expense_list.append(given_expense)

#Once all the expenses have been entered, first classify each expense:
#• Less than $25: Small expense
#• $25 through $100: Moderate expense
#• Greater than $100: Large expense

small_expense_count = 0
moderate_expense_count = 0
large_expense_count = 0

for expense in expense_list:
    if expense < 25:
        small_expense_count += 1
    elif expense <= 100:
        moderate_expense_count += 1
    else:
        large_expense_count += 1

#Then print out the results for user:
#• Total number of expenses
print(f"Total number of expenses: {len(expense_list)}")

#• Total expenses
print(f"Total expenses: ${sum(expense_list):,.2f}")

#• Average expense
print(f"Average expense: ${(sum(expense_list) / len(expense_list)):,.2f}")

#• Smallest expense
print(f"Smallest expense: ${min(expense_list):,.2f}")

#• Largest expense
print(f"Largest expense: ${max(expense_list):,.2f}")

#• Number of small, medium, and large expenses
print(f"Number of small expenses: {small_expense_count}")
print(f"Number of moderate expenses: {moderate_expense_count}")
print(f"Number of large expenses: {large_expense_count}")


#Make sure to format all the dollar amounts properly.