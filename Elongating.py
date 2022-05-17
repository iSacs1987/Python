"""
This is the example script that shows how you can elongate your lists with the
help of the list methods apend and extend. Both methods are run in-place, that
means the changes you make on your list are executed immediatly. To use these
list methods we have to work with the point notation as it will be explained
down below.
"""
# First we have to create two lists. Here I use the examples we already saw
# when we were talking about range
list2 = list(range(5,20))
print("Our First list:\n",list2)
list3 = list(range(3,40,3))
print("Our Second list:\n",list3)
# Now I can use the list method append, to hand over my list3 as a new element
# for my list2. The code shown below works in-place and on list2, so that means
# since we wrote the name of our first list before the point Python now knows
# that we want to make changes on list2. Than we specify the method we want to
# use, in our case the append method and hand over the variable or value we want
# to add as a new element to the end of list2. In case of the example below our
# list3 is now at index 15 in our list2
list2.append(list3)
# Now I print out the result of the append method
print("The lists after using append:\n",list2)
print("The element at index 15 of list2:\n",list2[15])
print("The length of our appended list2:",len(list2))
# I reset the first list here to show you the difference between append and
# extend
list2 = list(range(5,20))
print("Our resetted First list:\n",list2)
# Now we use the extend method, again we work in-place and make changes directly
# to our list2. The extend method, in contrast to append(), loops over the
# contents of the handed over argument, here list3, and puts each element at the
# end of list2. So you have to make sure to use extend always in combination
# with a list (or some other kind of iterable data structure, more about that
# later). So what happens here is that at the end of list2, after the 19, the
# elements of list3 (3,6,9 ... until 39) are added as new elements to our list2
list2.extend(list3)
print("The lists after using extend:\n",list2)
print("The length of our extended list2:",len(list2))
# We can use append with the help of single elements as well. So for example if
# we want to add the number 100 to the end of our list2 we would use:
list2.append(100)
# Or if we want to append just a single element of list3 to our list2 we would
# use the following:
list2.append(list3[5])
print(f"List2 after appending 100 and {list3[5]}:\n{list2}")
