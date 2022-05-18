"""
This is the example script for working with the insert method. As always than
using these methods with point notation it works in place and changes your list
permanently
"""
# We have again our trusty list
list2 = list(range(5, 20))
print("Our list looks like this:\n", list2, "\n")
# Now I define two integer variables that I want to use to insert them into my
# list
insert1 = 100
insert2 = 0
# First I want to insert the variable insert1 at index 3 in my list
list2.insert(3, insert1)
print(f"Inserting {insert1} at index 3 returns:\n {list2} \n")
# Now I want to insert the variable insert2 before the last element of my list
# To do this I can use the index -1 as position to insert into my list
list2.insert(-1, insert2)
print(f"Inserting {insert2} before the last element returns:\n {list2} \n")
# If we use a smaller negative number, e.g -3 we can insert things before the
# nth to last element. That means -3 leads to an insert before the third to last
# entry in our list
list2.insert(-3, 4)
print("Inserting 4 before the third to last entry returns:\n", list2, "\n")
# Last but not least we can insert at the end of our list by using len(list2)
# as the position to insert something. Normally you would use append() but it
# also works with insert
list2.insert(len(list2), 40)
print(f"Inserting 40 at position {len(list2)} returns:\n {list2}")
