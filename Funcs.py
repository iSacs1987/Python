"""
This is the example program for working with functions in Python. It shows you
how to define functions with signatures (def keyword), how to call-back them
inside your main program and the behavior of variables inside and outside of
functions (namespace for global and local variables)
"""
# To show you how the namespace of variables outside an dinside of functions
# work I included a small global variable called result here. Keep in mind that
# all variables we define in our main program, that means outside of functions
# are called global variables.
result = 200
# To show you the behavior of global and local variables, I included this print
# statement multiple times over the course of this program
print("Result:", result)
# Now we can create the signature of our function with the keyword def. This
# keyword is followed by the name of our function (sum_up) and () and a :
# If our function should take parameters or arguments, we have to put them in
# our brackets. That means here the function sum_up takes two arguments called
# a and b. Normally you would use names that are more descriptive to make clear
# what kind of datatype you expect.
def sum_up(a, b):
    # Now we can write down the code we want to executed during a call back of
    # our function. Please remember that call back means the execution of our
    # function inside the main program. This simple example takes the parameters
    # a and b and than calculates the sum of them. To do this we use a local
    # variable called result as well and assign it the value of a+b
    result = a + b
    # Now I included the result print out here to show you how local and global
    # variables behave during the execution of a loop.
    print("Result:", result)
    # To make sure that the calculated value is available to us in the main
    # program we have to hand it back to it with the help of a return statement
    # If we don't do this the value would only be available during the run of
    # our function, since its a local variable. As soon as Python encounters a
    # return (or the indented part stops), it knows that the function ends here
    return result


# After we defined our function we can go on with the rest of our main program.
# In this part of our code we can now include our call backs. I included several
# different examples. The first one uses the function to assign a value to a new
# global variable test. That means the value of the local variable result is
# assigned to the global variable test with the help of our return statement in
# line 36.
test = sum_up(5, 9)  # ==> calculates 5 + 9  and returns 14
# Now we can use the newly assigned global variable test, just as we saw with
# other variables beforehand.
print(test)
# Again I include the result print out to show you the behavior of global and
# local variables here.
print("Result:", result)
# I can use the call back of my functions inside of other functions or methods
# as well, as long as I return something. That means a function without a return
# statement would NOT lead to a nice print out.
print(sum_up(3, 8))  # sum_up(3,8) is replaced with 11 here
# Now I want to show you what happens if we assign the return value of our local
# variable result to our global variable result with the help of a call back of
# our function. Now we change the value of our global variable result
# permanentely since we create a new assignment.
result = sum_up(7, 10)
print("Result:", result)
# Last but not least we can include the call backs of our functions inside of
# loops as well. Here I created a nested loop, where both iterators run from 0
# up until 9.
for i in range(10):  # Outer loop
    for j in range(10):  # Inner loop
        # for each combination of my two iterators i and j, I now call back my
        # function and print out the returned value.
        print(sum_up(i, j))
