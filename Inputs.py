"""
This is our second example program for using input and casting of variables.
We learned that we can get user inputs by using the built-in method input
"""
# First we want to get some inputs from the user. If we use input() without a
# string in the brackets, the user has to type something in, but he doesn't get
# any message of what is expected from him. Therefore use input always with a
# string like "Give me a Number" or "Number" or "Type in", so that the user
# knows what you want from him. here we declare four different variables that
# get their value directly from the user input
test_number1 = input()
test_number2 = input("Give me a number: ")
hello = input("Type in something: ")
world = input("Type something else: ")
# Now we want to print out the inputs from the user. We can do this simply with
# the print command as we learned earlier.
print(hello)
print(world)
print(hello,world)
# When using input we have to keep in mind that the values we got from the user
# are strings. That means even if the user types in 5 for example the value of
# our variable is "5" in form of a string and not in form of an integer. So to
# change the data type (variable type) of these inputs we have to cast them to
# the corresponding type. We can use this with the methods int(), float() or
# str() for our main data types. So down below we cast our input test_number1
# to an integer (whole number like 5, 3 or so). Please keep in mind that you run
# into an error if you hand over something like "Hello" or "7.9" to this method.
print(int(test_number1))
# The second example I included here casts our input test_number2 first to a
# float and than to an integer. That means the operations are run inside out.
# Here we can hand over something like "5" as well as something like "7.9" to
# get an integer, because the int() method is able to cast floats to integers.
# Please keep in mind that int() doesn't round so int(7.9) results in 7 and not
# 8 since everything after the whole number is just cut off.
print(int(float(test_number2)))
