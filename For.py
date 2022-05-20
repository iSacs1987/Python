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

# list1 = ["Hello", "World", "How", "Are", "You"]
# for elem in list1:
#     print(elem)
