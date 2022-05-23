"""
This is the example program to show you the definition and usage of functions
with multiple return values. It shows you how to work with this kind of things
in a simple way by using a function that calculates an addition and a
subtraction of two integers.
"""
# So we define our function in a similiar way as we already saw multiple times
# when working with these functions
def mathfunc(a, b):  # a=12 and b=15 using call back in line 10
    # Now I can define my two local variables sumup and subtrac that get
    # assigned values according to the calculations I want to run in this
    # function. That means sumup gets assigned the value that is the sum of a
    # and b, while subtrac gets assigned the value that is a subtracted by b.
    sumup = a + b  # 12 + 15
    subtrac = a - b  # 12 - 15
    # Now I can return my local variables by writing a return statement and
    # add the corresponding local variables to it by simply separating them with
    # a comma.
    return sumup, subtrac  # ==> returns 27 and -3 for a=12 and b=15


# Here I define three global variables so that I can create three call backs
# of my function later on.
variable1 = 12
variable2 = 15
variable3 = 7
# Now I create my three call backs with the different global variables. Instead
# of assigning the result of my function to just one new variable, I now have to
# assign it to two variables, since my function has two return values. Keep in
# mind that the order stays always the same. That means the first new variable
# (result1, result3 or result5) is always assigned the value of sumup from my
# function and the second variable (resul2, result4 or result6) is always
# assigned the value of subtrac from my function.
result1, result2 = mathfunc(variable1, variable2)  # mathfunc(12,15)
result3, result4 = mathfunc(variable1, variable3)  # mathfunc(12,7)
result5, result6 = mathfunc(variable2, variable3)  # mathfunc(15,7)
# Now I can print out my newly assigned global variables, with the help of
# f-strings for example.
print(f"The Addition of {variable1} and {variable2} results in {result1}")
print(f"The Subtraction of {variable2} from {variable1} results in {result2}")
print(f"The Addition of {variable1} and {variable3} results in {result3}")
print(f"The Subtraction of {variable3} from {variable1} results in {result4}")
print(f"The Addition of {variable2} and {variable3} results in {result5}")
print(f"The Subtraction of {variable3} from {variable2} results in {result6}")
