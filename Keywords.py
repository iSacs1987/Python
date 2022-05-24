"""
This is the example program for working with the keywords pass, break and
continue. Pass can be used as a place holder for testing out your loops and
if statements without having to put code inside of your statements. Break allows
us to stop a loop and go on with the code after our loop. Continue breaks out
of the current iteration and stops the execution of any kind of code that comes
after the continue statement.
"""
# First I have to generate a list for my loop
list1 = list(range(25))
# Now I create a simple loop that iterates over my lists
for elem in list1:
    # I include a print out to see what happens
    print(elem)
    # First I create a statement that can be True at some point in time, but
    # since I don't know what I want to do here I just put a pass in it, so that
    # I don't have an empty if statement
    if elem > 10:
        # Pass allows us to have "empty" if statement, loops and so on, but
        # please use this only in combination with comments, so that you know
        # what kind of calculations you want to add to your statement later on.
        pass
    # Now I included a statement to terminate my loop as soon as I encounter a
    # specific number (here 20)
    if elem == 20:
        # The statement break terminates the most inner current loop of your
        # program. That means here, since we have just one for loop this loop
        # stops here as soon as break is encountered. If we would have nested
        # loops (2 or more loops inside each other) we would only stop the most
        # inner one and the outer loop would still go on to the next iteration
        # and restart the inner loop as we learned beforehand.
        break
    # This third if statement was included to show you the usage of continue.
    if elem > 15:
        # As soon as we hit numbers that are greater than 15 we will com into
        # this if statement here and Python will encounter the continue keyword.
        # This means the program jumps back to the beginning of the loop in line
        # 12 and the code that comes after this statement (is below it) won't
        # be executed anymore. That means for numbers 16,17,18,19 and 20 we
        # don't get the print out "End of Loop"
        continue
    # This second print statement was included to show you how the behavior of
    # the loop changes when encountering continue and break.
    print("End of Loop")
