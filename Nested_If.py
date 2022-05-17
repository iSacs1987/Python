"""
This is the exampel program for working with nested if statements. Here I
created a nested if statement and combined the same checks with an and in a
second if statement
"""
# First we have to get the inputs from the user. So here I ask for four
# different numbers and cast them directly into integer
input_number1 = int(input("Number 1 of 4: "))
input_number2 = int(input("Number 2 of 4: "))
input_number3 = int(input("Number 3 of 4: "))
input_number4 = int(input("Number 4 of 4: "))
# Now I can create my nested if statement. We use this construct if we have
# instructions (or code) that should be executed when both checks are True
# while we also have code that should be executed if only the first statement
# returns true. So we first check the condition of number1 and number2 being
# equal
if input_number1 == input_number2:
    # Now we can run the code that depends only on our first condition. This
    # means that the print command below is executed whether the if in line 25
    # is True or False.
    print("Your first two numbers are identical, Wow")
    # Now we make our second check. Please keep in mind that this if-clause is
    # only tested if the check in line 17 returned True, otherwise we are NOT
    # inside of this if statement.
    if input_number3 == input_number4:
        # Now we can execute code that depends on both statements to be true
        # Don't forget to always put some code inside your if, elif, else
        # statements because Python does NOT allow empty if, elif, else clauses
        print("Your numbers three and four are also identical")
# This second example is the same as in Logics.py So that means the code in line
# 33 is only executed if both checks are True
if input_number1 == input_number2 and input_number3 == input_number4:
    # This block of code is analogous to the block in line 29 as it's also
    # dependent on both of our checks. The main difference between these two
    # constructs is that here we don't have any way of running code that only
    # depends on our first statement to be true
    print("Twice, the same number really?")
