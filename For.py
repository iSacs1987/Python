"""
This is the example program for working with for loops in Python. The creation
of these loops is pretty simple.
"""
# I want to create a loop that sums up all elements in a specific range. To be
# able to do this, I have to define a variable that can be the sum first.
sum = 0
# Now I can create my for loop by using the line shown below. This line tells
# Python to take a variable called i, that starts with a value of 0 and use it
# repetitively. So i starts at 0, than we print out this value (line 24), add
# this value to our sum (line 25) and than we go back to line 17, increse i by
# 1 and start over. So now we print out the value 1 (line 24 again) and add 1
# to our sum (line 25 again). This process is repeated until the value of i
# reaches 19. As soon as we finished with the print out of the value 19 in
# line 24 and the addition in line 25, we leave the loop and now the code that
# comes after our loop and is not indented is executed.Please make sure that you
# don't forget the ":" after your range or you get syntax errors.
for i in range(20):
    # to execute code inside a loop we have to indent is, just like we saw with
    # our if statements. The complete block of code that is at the same
    # indentation level (line 24 and line 25) is exectued during each iteration
    # of the loop. As soon as python encounters code that is NOT indented it
    # recognizes the end of the block and goes back to the top of the loop.
    print(f"We are at iteration {i+1} of 20")
    sum += i  # 0+1+2+3+4+5+6+..+19
# This part of our code is only executed after we finished running through all
# iterations of our loop.
print("The sum of number 0 up untl 19 is", sum)

# Another way of using for loops is by iterating over lists (or other iterables
# like dictionaries, sets or tuples) in a form of "for each" loop.  To use this
# we have to define a list first
list1 = ["Hello", "World", 5, 6, "How", "Are", 7.9, 2.7, "You"]
# Now we can create our loop in a similar manner to the exampel we saw above.
# but this time instead of using the running index i we use a loop variable
# called elem to mark the difference between a normal for loop and a for each
# loop here. Furthermore instead of putting a range at the end of the
# constructor we put the list we want to use here. That means elem is a variable
# That is assigned the value "Hello" in our first iteration. After the all code
# inside the loop is executed, the program jumps back to the top of the loop
# and now elem is assgined the value "World". Again the code is executed and
# afterwards the program jumps back to the top. This is repeated until elem was
# assigned all values that were part of our list.
for elem in list1:
    # Here I included just simple print statements for you to see how this works
    # First I print out the loop variable elem and than the type of the current
    # value of elem.
    print(elem)
    print(type(elem))
