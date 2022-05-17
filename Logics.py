"""
This is the exampkle program for working with logic operators and/or in Python.
It can also work as some kind of example solution for exercise 6
"""
# First we get the input from the user and cast it directly into an integer
# For the example here I included the numbers I typed into my terminal as
# comments behind each line
input_number1 = int(input("Number 1 of 4: ")) #5
input_number2 = int(input("Number 2 of 4: ")) #4
input_number3 = int(input("Number 3 of 4: ")) #5
input_number4 = int(input("Number 4 of 4: ")) #5
# Now we can create our two if-clauses to compare our input with each other.
# The program first checks our two statements in the brackets, comparing our
# input_numbers with each other and than combines them using the logic operator
# and. So the whole line would return True only if both statements are True
# So for our example we get the returns shown below:
# False and True ==> False
# Since our first statement was False the whole line returns False, since both
# statements have to be True so that and can return True for the whole line
if (input_number1 == input_number2) and (input_number3 == input_number4):
    print("Twice, the same number really?")
# For our second example I combined my two statements using an or operator
# This means the whole line returns True if at least one of our two statements
# returns True. So for this example the return looks like it's shown below
# False or True ==> True
# As you can see we don't need to use brackets around our statements, but you
# can use them, if it helps you to create a better overview of your code.
if input_number1 == input_number2 or input_number3 == input_number4:
    print("At least one duplicate number, you aren't creative, are you?")
