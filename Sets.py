"""
This is the example script for working with sets. It shows you how to create
sets, how to cast them to lists to remove duplicate values from lists and how
you can add or remove elements from your sets
"""
# We can create sets with the help of curly brackets {}, but we can't have an
# empty set. That means if you write something like set1 = {} Python directly
# assumes you want to create a dictionary. So your sets need to have at least
# one element at least and again if you have only one element you need to add a
# comma afterwards to make sure that the set is generated
set1 = {"Hello", "World", "How", "Are", "You"}
print("type of set1:", type(set1))
print("This is set1:", set1)
# Just like with tuples we can use the range) method to generate our sets, but
# of course we have to cast it to a set to make this possible.
set2 = set(range(10))
print("type of set2:", type(set2))
# Interestingly the order of the elements inside this set seems to be always
# the same, even though it should change with different calls.
print("This is set2:", set2)
# Last but not least I want to show you how you can use sets to remove duplicate
# values from lists. Since sets don't allow duplicates we can cast a list with
# duplicate values as seen for list1 to a set to remove duplicates.
list1 = [5, 6, 7, 8, 5, 1, 2, 5, 9, 4, 6]
print("This is list1:", list1)
# Now we cast our list to a set
set3 = set(list1)
print("type of set3:", type(set3))
print("This is set3:", set3)
# If we now cast our set to a list again, we get a list without duplicate values
list2 = list(set3)
print("type of list2:", type(list2))
print("This is list2:", list2)
# You can use a short version by doing everything in one line as shown below
list1 = list(set(list1))
print("This is the new list1:", list1)
# We can remove elements at random from our sets with the pop() method. This
# method takes an element of our set and hands it over to us, so that we can
# assign it to a new variable
print(set2)
element1 = set2.pop()
print(set2)
element2 = set2.pop()
print(set2)
# We can also add elements to our sets by using the add() method and hand over
# the value we want to add to our set as an argument.
set2.add(element1)
print(set2)
set2.add(element2)
print(set2)
set2.pop()
print(set2)
# Last but not least there are the methods discard() and remove() that delete
# elements that are handed over as arguments to them in place from the specified
# set. That means these changes are permanently.
set1.discard("You")
print(set1)
set1.remove("Are")
print(set1)
# What I want you to take back with you when working with sets is line 35, that
# means the usage of set to create a list that doesn't contain any duplicates.
