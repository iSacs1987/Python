"""
This is the example script for different list methods I showed to you in my
presentation.
"""
# First I create a mixed up list that contains different integers
list = [1, 5, 7, 9, 5, 9, 5, 1, 6, 6, 10, 38, 2]
print("Ourlist looks like tis:\n", list, "\n")
# Now I use the index() method which takes one argument and hands back the first
# position() at which the corresponding element was found in our list. So for
# the example here the return would be 1 since the number 5 can found the first
# time at index 1 in our list. If you use index() with a value that is NOT in
# your list you get an error, so please keep this in mind.
print("The number first is found first at index", list.index(5))
# While index is a so-called list method, that's why we need to use the point
# notation, max and min work on the list, that means they take the list as an
# argument and return the maximum (max) or minimum (min) value respectively
print("The maximum value of our list is", max(list))
print("The minimum value of our list is", min(list))
# The list method count() takes again an argument and how often this argument
# can be found in our list. In comparison to index, handing over an argument
# that is NOT part of our list, does NOT return an error but a simple 0.
print(f"The number 5 can be found {list.count(5)} times in our list")
print(f"The number 20 can be found {list.count(20)} times in our list")
# Next I want to show you two methods that again work in place and thus change
# your list permanently. So use these methods only if your really need to change
# the order of the elements in your list. The first method is reverse which, as
# the name implies, reverses the order of your list
list.reverse()
print("\nThe reversed list looks like this:\n", list, "\n")
# The second method is sort() which sorts our list in place in ascending order
# As always these methods that work in place don't return a value and thus we
# can't use them in other methods, that means print(list.sort()) would give
# the printout None.
list.sort()
print("The sorted list looks like this:\n", list, "\n")
# If you want to sort your list in DESCENDING order you can use the sort()
# method with the argument reverse=True as shown below, or you could use
# list.sort() first and than list.reverse() as two separate commands
list.sort(reverse=True)
print("The newly sorted list looks like this:\n", list, "\n")
# Now I want to talk about copy and making changes to the list. If you want to
# assign a new variable with an existing list,make sure to always use copy() as
# it is shown below, because now you have two variables that are independent
# from each other.
list_new1 = list.copy()
print("The copied list looks like this:\n", list_new1, "\n")
# If you use a simple assignment as it's shown below you create a new variable
# called list_new2 but this variable npow points to the same place in the memory
# as list. That means any changes you make on list are also done on list_new2
# and vice versa. BE CAREFUL!!!!!
list_new2 = list
print("The newly assinged list looks like this:\n", list_new2, "\n")
# If we now make changes to our variable list, let's say we remove the element
# 10 from it we can see that the 10 is deleted from list and list_new2 while
# list_new1 stays unchanged.
list.remove(10)
print("After using list.remove(10) our lists look like this:")
print(list)
print(list_new1)
print(list_new2, "\n")
# The last method I want to show you is the clear() method. This DELETES all
# elements in your list and leaves you with an empty list. Again this method
# works in place an makes permanent changes. BE CAREFUL!!!!
# I used the method here on list_new2 to show you that now the reverse of the
# example above with remove happens. So now even though I used clear on
# list_new2, the elements of list were also deleted.
list_new2.clear()
print("After using list_new2.clear() our lists look like this:\n")
print(list)
print(list_new1)
print(list_new2)
