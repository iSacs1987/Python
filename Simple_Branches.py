"""
This is the example program for generating simple if-clauses. This program
compares the name inputted by the user with three different strings
"""
# First we have to get the input from the user
input_string = input("Type in a Name please (first and last): ")
# Now we can construct our if-clause. First we compare the value of our variable
# string_input with the string "Olaf Scholz". Please keep in mind that these
# comparisons are cas sensitive. We have to use the == operator here to check
# for identity or in case of numbers for mathematical equalness. So this is
# different from the = we use to assign our variables. Don#t forget to close
# your predicate with the ":".
if input_string == "Olaf Scholz":
    # If the check above, the comparison of the value of our variable with the
    # String is True, the code (or instructions) which are below the if clause
    # are executed. You have to make sure that the whole code block is indented
    # as it's seen here, otherwise the code wouldn't be executed. Only blocks of
    # code that have the same indentation are executed after the if clause.
    # Everything that has no indentation, like the elif below is outside of our
    # if clause
    print("Our chancellor, really")
# Only after python compared the value of our variable with the first string and
# came to the conclusion that they are NOT identical, so the statement in line
# 13 was False, these elif statements are executed. That means if the statement
# in line 13 was True, the program would execute the code in line 21 and than
# go otu of the if clause and run the command print("The End").
elif input_string == "Anna-Lena Baerbock":
    # Now if the statement in line 26 was True, the block of code that is under
    # our statement can be executed. Again you have to make sure that everything
    # has the same indentation. As soon as you have code that has no indentation
    # and is not part of the if clause (if, elif or else) you leave your if
    # clause.
    print("The foreign minister, are you sure?")
# We can combine as many elif statements as we want together, to create a more
# complex if clause. Keep in mind that these checks are run in succession, that
# means if you want to have if clauses that are NOT related to each other, it's
# better to use separate if clauses for them.
elif input_string == "Christian Lindner":
    print("The party of the better situated, ok")
# Only after python ran the checks in line 13, line 27 & line 38 and found that
# all three were False, than the block of code that is beneath the else
# statement is executed. That means as long as one of the three checks above
# returns a True, the code shown in line 45 is not executed.
else:
    print("I don't know this person")
# As mentioned above as soon as you have code that has no indentation, as it's
# shown with the print command down below, this signales python that your if
# clause is finished. So the code below is executed indepently of the results
# of the different checks done above.
print("The End")
