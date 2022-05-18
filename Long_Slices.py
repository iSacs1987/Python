"""
This is the example I showed during our second lesson, when we were talking
about using slices with numbers that are out of range
"""
# We create a list with range
list2 = list(range(20))
# Now we use a slice that contains a number that is out of range for this list
# and get the whole list back, without running into an error
print(list2[:22])
# if we start our slice with an index that is out of range, we get an empty list
print(list2[22:])
# Last but not least if we define a stepsize that is bigger than our whole list
# we get a list that contains only the first entry of our original list
print(list2[::22])
