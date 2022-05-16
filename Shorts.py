"""
This example program shows the usage of short cuts for the four mathematical
standard operations Addition, Subtraction, Multiplication and Division
"""
# First I assign two variables to use here, both are integers
number1 = 7
number2 = 9
# To show you how these short cuts work, I will print out the value of number1
# step by step
print(f"at the beginning number1 has a value of {number1}")
# Now I increase the value of number1 by 1 and print out the result afterwards
number1 += 1
print(f"number1 increased by 1 is {number1}")
# Now I decrease the value of number1 by 3
number1 -= 3
print(f"the new number1 reduced by 3 equals {number1}")
# Now I multiply number1 by 4
number1 *= 4
print(f"the new number1 multiplied by 4 equals {number1}")
# In the next step I add the value of number2 to my number1
number1 += number2
print(f"the new number1 increased by {number2} produces {number1}")
# Last but not least I divide number1 by 3
number1 /= 3
print(f"the new number1 divided by 3 results in {number1}")
