"""
This is the second example program for working with if clauses. Here I
included some different operators like > or >= to show you how to use them.
"""
# First we get two inputs from the user and cast the first one to an integer
# while we leave the second one as a string
input_number = int(input("Type in a number: "))
input_string = input("Now I need a string: ")
# Now I create my first simple if statement. I ask if the number the user handed
# over is greater than 10.
if input_number > 10:
    # If input_number has a value of at least 11 the print statement below
    # is executed
    print("Your input was greater than 10")
else:
    # if input_number has a value of 10 or less the print statement below is
    # executed
    print("A pretty small number")
# Now I create a second if clause, to compare my String with another string as
# we saw for our first exampel and for exercise 4. So the general concept should
# be clear here and thus I won't explain it any more.
if input_string == "Hello":
    print("How uncreative")
else:
    print("we are a Clown, aren't we")
# The last if clause I created contains again an if and two elifs, to check
# how big the value of input_numnber is. If it has a value of at least 1000
# the code in line 33 is executed if the value is between 100 and 999 the code
# in line 35 is executed, if the value is between 10 and 99, so has two digits
# the code in line 39 is executed and last but not least if the value is below
# 10, so only 1 digit the code in line 41 is executed.
if input_number > 999:
    print("You really like big numbers, don't you?")
elif input_number > 99:
    print("Still in the triple digits, nice choice")
elif input_number >= 10:
    # Please keep in mind that a value of 10 also fulfills the criteria above
    # since we now check for greater than or equal
    print("Only two digits, this poor poor number")
else:
    print("A single digit, I'm sorry for your number")
