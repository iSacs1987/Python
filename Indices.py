"""
This example program shows you the usage of Indices in combination with lists
and thereby especially the usage of some special indices like -1
"""
# First we generate our two trusty lists
list2 = list(range(5,20))
print("Our first list:\n",list2)
list3 = list(range(3,40,3))
print("Our second list:\n",list3)
# Now we can access the first and the fourth element of our lists by using
# the indices 0 and 3
print("Element at index 0 of list2:",list2[0])
print("Element at index 3 of list2:",list2[3])
# To access the last element of a list we could use the complex solution to use
# the len method and subtract 1 from the result to have the number of the last
# index, because if you think back a list with 10 entries has a len of 10 but
# the last index is 9
print("Last Element of list2 with len:",list2[len(list2)-1])
# Python offers us a simpelr solution to this problem by simply using the index
# -1 which represents the last element of our list
print("Last Element of list2 with -1:",list2[-1])
# We even can use this method to access the nth to last element of a list
# So by using -3 we can access the third to last element of list2
print("Third to last element of list2:",list2[-3])
# Now I combine my lists to have a bigger list at my disposal and to show you
# how the last element of list2 changed after the usage of extend()
list2.extend(list3)
# If I now access the new last Element of list2 I get the following
print("New last Element of extended list2:",list2[-1])
# As mentioned above we can use negative indices to access the nth to last
# element so if we want to access the tenth to last Element we can use -10
print("Tenth to last element of extended list2:",list2[-10])
