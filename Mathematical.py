"""
This is the third example program, that shows you how to use the seven different
mathematical operation Addition, Subtraction, Multiplication, Division,
Integer Division, Power and Remainder.
"""
# First we define 2 interger variables witht he values of 45 and 7
number1 = 45
number2 = 7
# Now we can run all the mathematical operations we talked about. I use these
# operations to assign the result to new variables called result1 up to result7
# The first new variable thus has the value of 45+7
result1 = number1 + number2
# The second variable now has the value of 45-7
result2 = number1 - number2
# The third variable now has the value of 45*7
result3 = number1 * number2
# The fourth variable now has the value of 45/7
result4 = number1 / number2
# While the first four operations are pretty standard, since they are the
# general mathematical operations known to everybody, the other three operations
# are a bit mor complex. First the Integer division //. Here we calculate 45/7
# and than cast the result 6.428... to an integer value. Thus this fifth
# variable now contains the value 6
result5 = number1 // number2
# Our second more complex operation is called power, here we calculate 45^7, so
# that means the number before the ** is the base and the number after the **
# is the so called exponent. Thus our sixth variable contains now the stupidly
# big number 373669453125
result6 = number1 ** number2
# Last but not least we have the remainder operation. Here our seventh variable
# gets assigned the modulo (rest in german) of the division 45/7. That means
# the value assigned to this variable is 3
result7 = number1 % number2
# Now we can print out the results of our operations with the help of f-strings
# I included the special character \n in my strings here to create newlines.
# Everytime Python reads \n a line break is created in the print out.
print(f"The Addition of 45 and 7 yields:\n{result1}\n")
print(f"The Subtraction of 45 by 7 yields:\n{result2}\n")
print(f"The Multiplication of 45 by 7 yields:\n{result3}\n")
print(f"The Division of 45 by 7 yields:\n{result4}\n")
print(f"The Integer Division of 45 by 7 yields:\n{result5}\n")
print(f"45 powered by 7 yields:\n{result6}\n")
print(f"The Remainder of the Division of 45 by 7 yields:\n{result7}\n")
