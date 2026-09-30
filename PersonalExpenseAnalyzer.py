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

#Then print out the results for user:
#• Total number of expenses


#• Total expenses


#• Average expense


#• Smallest expense


#• Largest expense


#• Number of small, medium, and large expenses


#Make sure to format all the dollar amounts properly.