"""
This is the example script that explains the usage of range() and len
"""
# We can use range with one argument as shown below. This creates a range that
# contains the numbers 0,1,2,3,4,5,6,7,8 and 9 because the handed over end point
# of your range (here 10) is excluded from it.
list1 = range(10)
print("Using range with one argument:",list1)
print("Something seems fishy:",type(list1))
# The two print out above showed that we didn't get a list but a range. If we
# want to use this range as a lisst we have to cast it using the list() method
# as it's shown below
list1 = list(list1)
print("After casting:",list1)
print("This looks promising:",type(list1))
# We can use range with two arguments as well. Here the first argument (5) is
# the starting point of our range that is included and the second argument (20)
# is the end point of our range that is excluded. So the resulting list (we cast
# it directly here) contains integers from 5 up until 19
list2 = list(range(5,20))
print("Using range with two arguments:",list2)
# A third way to use range is by handing over three arguments to it. The first
# argument (3) is again the starting point, the second one (40) the excluded
# end point and the third one (3 again) is the step size. So now our new list
# contains the numbers 3,6,9 and so on up until 39
list3 = list(range(3,40,3))
print("Using range with three arguments",list3)
# We can create lists with negative entries by using negative numbers and a
# negative stepsize as well.
list4 = list(range(-3,-40,-3))
print("Using range with all negative numbers:",list4)
# To get a similiar result but with a different order we can use a negative
# starting point, that has to be smaller than the end point (here -40 and -3)
# and than use a positive stepsize. Now we can create a list that contains the
# numbers -40, -37, -34 until -4
list5 = list(range(-40,-3,3))
print("Using range with neg. numbers and pos. Step:",list5)
# Last but not least we can use range we a bigger number as starting point (40)
# and a smaller number as endpoint (3) if we use a negative stepsize (-3)
list6 = list(range(40,3,-3))
print("Using range from big to small:",list6)
# To check how long a list is we can use the len() method. Hand over the name
# of the list in question to this method and you get back an integer that tells
# you how many elements are in your list
print(len(list1)) # returns 10
print(len(list2)) # returns 15
print(len(list3)) # returns 13
# We can use the len() method to make sure that a specific index is part of our
# list. Let's say we have user input as shown below (8)
input = 8
# Now we want to make sure that this index is part of our list. So we can use
# an if statement as written below to see if the index is still in the range or
# not. Please keep in mind that we have to use either input <= len(list1)-1 or
# input < len(list1) because the maximal index for our list1 is 9 and the len()
# method returns 10. This has to do with the indexing starting at 0 in Python
if input <= len(list1)-1:
    print(f"The index {input} is inside the range of list1")
