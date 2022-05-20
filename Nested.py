"""
This is the example script for working with nested for loops. We can put two
into each other. To run multiple iterations after each other. This is good when
working with multi-dimensional lists for example or nested dictionaries. Because
Now we can have an outer loop over the outer list or dictionary and an inner
loop over the inner lists or dictionaries
"""
# Here I created an example with the help of two little ranges. Please keep in
# mind that range(10) produces something that looks like this
# (0,1,2,3,4,5,6,7,8,9). That means we create an iterable here that can be used
# by our loop and i, also called iterator, starts at value 0 and jumps from
# element for each iteration.
for i in range(10):  # ==> 0 until 9
    for j in range(15):  # ==> 0 until 14
        # Now I can use my two iterators (i and j) to give a small print out.
        # When you look at the printouts you will see that i and j start at 0
        # and than j is increasing from 0 until it reaches 14 while i stays at 0
        # Afterwards i jumps to 1 and now j starts again at 0 and increases
        # until it reaches 14 again. So What happens here? The program starts at
        # line 13 and sets i to 0, than it goes to line 14 and sets j to 0. Now
        # it goes to line 30 and 31 to generate the print outs. After these two
        # lines are executed it now jumps back to line 14 and sets j to 1 before
        # executing lines 30 nad 31 again. This process is repeated until j
        # reaches the end of hte range (j=14). Now after generating the prints
        # in lines 30 and 31 a last time, the program jumps back to line 13 and
        # set i to 1. Afterwards it goes to line 14 and resets j to 0, so that
        # the loop of print outs can start again but this time with starting
        # values of i=1 and j=0. This whole process is repeated until i reaches
        # also it's range end (i=9).
        print("Current iterations are i=", i, "and j=", j)
        print(i + j)
# This is the example matrix I handed over to you for our exercise 25.
matrix = [[1, 2, 3], [1, 5, 3], [1, 2, 3]]
