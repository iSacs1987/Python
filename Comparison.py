"""
This is our third example script for working with if clauses. This script
contains six different if clauses, all without an else to show you, that we
don't have to include an else to run our if clauses. That means for this
program, if the statement(s) are False nothing happens
"""
# Again I get two inputs from the user and cast them to integers right away
input_number1 = int(input("Number 1 of 2: "))
input_number2 = int(input("Number 2 of 2: "))
# Now I create my first if clause using an if and two elifs, to check for all
# possible relations two different numbers could have with each other. So I
# check if input_number1 is greater than inpu_number2 first, than I check if
# input_number1 is smaller than input_number2 and last but not least I check if
# they are equal to each other.
if input_number1 > input_number2:
    print("Wow your numbers decrease!")
elif input_number1 < input_number2:
    print("Wow your numbers increase!")
elif input_number1 == input_number2:
    print("The same number, really?")
# I included three additional if clauses that work with the different
# expressions I talked about. So first I check if input_number1 is greater than
# or equal to input_number2
if input_number1 >= input_number2:
    print("Your numbers could be identical, not vcery creative")
# Second I check if input_number1 is smaller than or equal input_number2
if input_number1 <= input_number2:
    print("Your numbers could be identical, not vcery creative")
# Last but not least I check if input_number1 is not equal to input_number2.
# That means as soon as input_number1 is greater or smaller than input_number2
# the statement below is True
if input_number1 != input_number2:
    print("You know two different numbers. Good for you!")
# Please keep in mind that the if clauses in line 24, 27 and 32 are independent
# from each other. That means each check is run here and if the result is True
# the corresponding print statement is executed. For example if input_number1
# has a value of 10 and input_number2 has a value of 5 the print commands in
# line 25 and line 33 would both be executed, since input_number1 has a value
# that is greater than input_number2 and thus the two numbers are also not equal
