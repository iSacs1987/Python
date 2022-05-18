"""
This is the example script for working with the remove method. Please keep in
mind that this method just like append and extend work in place and thus change
your list permanently.
"""
# We have again our trusty list
list2 = list(range(5, 20))
print("This is our list:\n", list2, "\n")
# Now we can remove some of the elements in our list. First we want to remove
# the number 8, simply by using remove(8). Don't forget that this works in place
list2.remove(8)
print("This is the list after removing the 8:\n", list2, "\n")
# In this second example we want to remove the element that is at index 6 of our
# now shorter list. For this example this means we remove the number 12 from
# our list.
list2.remove(list2[6])
print("This is the list after removing the element at index 6:\n", list2)
