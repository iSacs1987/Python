"""
This is the example script for working with math. Here I show you how to use the
different mathematical operations that are available to us in this module.
"""
# The omport is pretty simple
import math

# Here I define two variables which I want to use for my calculations
variable1 = 25
variable2 = 5
# Now I can use these mathematical functions to assign the calculated results as
# values for new variables. Please keep in mind that the returns are always of
# type float
result1 = math.isnan(variable1)  # Returns False because 25 is a number
result2 = math.exp(variable1)  # Returns e^25
result3 = math.log(variable1)  # Returns the logarithm of 25 to the base e
# Returns the logarithm of 25 to the base 5 ==> 2.0
result4 = math.log(variable1, variable2)
result5 = math.log2(variable1)  # Returns the logarithm of 25 to the base 2
result6 = math.log10(variable1)  # Returns the logarithm of 25 to the base 10
result7 = math.pow(variable1, variable2)  # Returns 25^5
result8 = math.sqrt(variable1)  # Returns the square root of 25 ==> 5.0
# Now we use the trigonometric functions sin, cos and tan. These methods assume
# that the argument we hand over is in radians. There are helper functions in
# math called degree() and radians() which convert your numbers. So degree takes
# a number in radians and returns the degree and radians takes a number in
# degree and returns it in radians.
result9 = math.sin(variable1)  # Calcu
result10 = math.cos(variable1)
result11 = math.tan(variable1)
# Now we can print out our results.
print(f"math.isnan({variable1}) returns: {result1}")
print(f"math.exp({variable1}) returns: {result2}")
print(f"math.log({variable1}) returns: {result3}")
print(f"math.log({variable1},{variable2}) returns: {result4}")
print(f"math.log2({variable1}) returns: {result5}")
print(f"math.log10({variable1}) returns: {result6}")
print(f"math.pow({variable1},{variable2}) returns: {result7}")
print(f"math.sqrt({variable1}) returns: {result8}")
print(f"math.cos({variable1}) returns: {result9}")
print(f"math.sin({variable1}) returns: {result10}")
print(f"math.tan({variable1}) returns: {result11}")
