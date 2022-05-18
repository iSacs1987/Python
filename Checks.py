"""
This is the example script for using in and not in to check whether something
is inside a list or not.
"""
# We create our trusty list
list2 = list(range(5, 20))
print("Our list looks like this:\n", list2, "\n")
# Now I define two simple integer variables to use them in my if-clauses
check1 = 12
check2 = 25
# Now I ask if check1 (12) is an element of my list2
if check1 in list2:
    # Since for this example 12 is in list2 we get the print out here inside
    # our if
    print("You found a number inside your own list. Genius!")
else:
    # If check1 would be something that is not part of our list, e.g. 25 we
    # would get the printout here in our else
    print("You don't know what numbers are in your list?")
# To show you the difference between "in" and "not in" I reversed the order of
# the printouts for this second if-clause. So here I ask if check2 (25) is NOT
# an element of my list2
if check2 not in list2:
    # Since for this example 25 is NOT part of list2 we get again the printout
    # here in our if-statement
    print("You don't know what numbers are in your list?")
else:
    # If check2 would be part of list2, e.g. 12 we would get the printout here
    # in our else
    print("You found a number inside your own list. Genius!")
