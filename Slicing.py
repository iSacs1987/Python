"""
This is the example script for generating slices of our lists with the help of
indices and colons.
"""
# We again generate our simple list
list2 = list(range(5,20))
print("Our list looks like this:\n",list2)
# Now we can generate slices of our list by using the method shown below. As I
# mentioned on my slices the general syntax is list[start_index:end_index] for
# these slices. Python cuts our existing list before the start_index and before
# the end_index, so that means the element at the end_index is excluded from
# our new list. Please note that we don't change our list2 here, we simply take
# a small part of it to look at or to define a new variable that contains this
# small part.
print("Slice starting at 0 and ending before 3 of list2:\n",list2[0:3])
print("Slice starting at 4 and ending before 8 of list2:\n",list2[4:8])
# If we use three elements inside our slice we can define the increment or step
# size of the slice
print("Starting at 2 and ending before 11 with step size 2:\n",list2[2:11:2])
# If we want to get the whole list starting at a specific index we can use
# either again a complex version with the help of len or we can just use n::
print("Everything starting at 3 until the end using len:\n",list2[3:len(list2)])
print("Everything starting at 3 until the end using '3::':\n",list2[3::])
# If we want only each nth element, e.g. each second element we can use a slice
# using ::n
print("Every second element:\n",list2[::2])
# If we want only the first n elements of a list we can exclude the 0 from our
# slice and just use :n
print("The first three Elements:\n",list2[:3])
# If we want only the last n elements of a list we can use either -n:: or -n:
print("The last three Elements using 'n::':\n",list2[-3::])
print("The last four Elements using 'n:':\n",list2[-4:])
# If we want a slice that excludes the last n elements we can use :-n
print("Without the last three Elements:\n",list2[:-3])
# If we want to generate a reversed list we can use the slice ::-1 of our list
print("The reversed list:\n",list2[::-1])
# Last but not least we can get a reversed list with only each nth element
# starting from our last element by using ::-n
print("Only each third element of the reversed list:\n",list2[::-3])
