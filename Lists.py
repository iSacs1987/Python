"""
This is the example script for creating lists, accessing specific elements in a
list and the usage of the method type()
"""
# To create lists we have to declare them in a way that is similiar to declaring
# our variables before. So we need a name of our choice (here list1 for example)
# than we assign the values to it with the help of an "="-sign. To tell Python
# that we want to create a list we need to use the square bracket [ and ]. We
# can create empty lists by using only the square brackets without anything else
# in them. But for now we want to create lists with contents, so we hand over
# the corresponding elements inside the brackets, separated by Comma.
list5 = []
list1 = [1,2,3,4,5,6]
list2 = ["Hello","World","How","are","you","?"]
list3 = [1.1,2.2,3.3,4.4,5.5,6.6,7.7]
# Now we can print out our lists
print("The empty list:",list5)
print("The integer list:",list1)
print("The string list:",list2)
print("The floating point list:",list3)
# We can use the method type to find out the data structure type as well as the
# variable type, farther down. Just use type() and put the name of the list or
# the variable inside the brackets.
print("Type of list1:",type(list1))
print("Type of list2:",type(list2))
print("Type of list3:",type(list3))
# Since only our list has a name and the elements are NOT named we have to
# access them using [] and the corresponding position in the list. That means
# lists are ordered and the indexing (Number of the positions) starts at 0. So
# the first element has the index 0, the second one has the index 1 and so on.
# So here I print out the second element of list2 and the sixth element of list1
# Please keep in mind to stay inside the boundaries of your list. That means
# list1[6] would return an Error
print("Second Element of list2:",list2[1])
print("Sixth Element of list5:",list1[5])
# We can also mix up the data types of the primitives we hand over on creation
# of our lists. So here I create a list that contains integers, strings and
# floating point numbers.
list4 = [4,5,"Hello","World",6.6,7.7]
print("The mixed list:",list4)
print("Type of list4:",type(list4))
# We can use type on a specific element of our list as well, we just have to use
# the corresponding index again, to work with the specified element, here we
# want the type of the third Element of our mixed list 
print("Type of the third Element of list4:",type(list4[2]))
