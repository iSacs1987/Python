"""
This is the example program for using try and except. With this method we can
catch errors and make sure that our program is NOT stopped whe encountering
errors. I created two separate try/except constructs but you could combine them
in one big construct as well as we saw during our course.
You could use except without an specific Error but I would NOT recommend this
because than you do NOT know what kind of Error you encountered. Thus it's
better to use except in combination with a specific type of Error.
"""
# This first try/except construct takes an input from the user and tries to
# cast it to an integer
try:
    # The program tries to execute everything inside our try
    number1 = int(input("Give me a number: "))
except ValueError:
    # if the code in line 14 produced an error, because he handed over a String
    # or a floating point number (which can't be casted to integer from string)
    # than the code inside our except is executed. That means as long as the
    # user typed in a whole number in line 14 we won't see the print out in line
    # 21
    print("Hey I wanted a number")
    number1 = 100
else:
    # If the code in line 14 was executed without raising an Error, than the
    # code inside our else statement is executed. That means the print out in
    # line 27 is only shown when the user typed in a whole number in line 14
    print("Nice Number")
# A second variable for our division
number2 = 100
# Here I create a second try/except construct, but this time I also included
# a finally statement.
try:
    # We try to execute this simple division, which only produces an Error if
    # number1 would be 0
    result = number2 / number1
except ZeroDivisionError:
    # If number1 was 0 the code in line 35 produces a ZeroDivisionError which we
    # can catch with our except statement.
    print("This is mathematical bullshit")
else:
    # If number1 was NOT 0 than the division in line 35 could be exectued with
    # out any Errors and thus we can print out our result here.
    print(result)
finally:
    # Independently of whether the code in line 35 produced an Error or not
    # everything we put into our finally statement is executed. This part of our
    # program is executed even if we encounter an Error we didn't catch with the
    # except statements.
    print("We are finished")
