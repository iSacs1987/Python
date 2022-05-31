"""
This is the second example script for working with try/except. Here we raise
our own Error
"""
# We create a simple try/except statement here
try:
    # We try to execute the code her
    input1  = int(input("Your number? "))
    # Now we check whether the input from the user is inside the range we
    # defined or NOT. If the user chose a number that is outside our range <1
    # or >5 when we raise an Error
    if input1 not in [1,2,3,4,5]:
        # As soon as the if statement in line 12 returns True the line below is
        # executed. With the help of the raise keyword we can generate our own
        # Error and thus can make sure we execute anything inside our except
        # statement
        raise RuntimeError
except RuntimeError:
    # This print command is only exectued if the statement in line 12 returned
    # and thus the RuntimeError was raised. That means as soon as the uses types
    # in a number <1 or >5 we get this print out. Be careful we do NOT catch
    # any other Errors here. That means our program is still stopped if the user
    # types in a String or a floating point number.
    print("Input outside of range")
