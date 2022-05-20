"""
This is the example program for working with tuples. It shows you how to
create tuples, how to access elements of tuples and what you have to careful of.
"""
# We can create a tuple simply by using normal brackets () and writing the
# corresponding elements into them. Please make sure to use a Comma (,) between
# your elements as a sperator
tuple1 = ("Hello", "World", "How", "Are", "You")
# Now we can print out the data type of our variable tuple1 as well as the
# variable itself
print("tuple1 is of type:", type(tuple1))
print("This is tuple1:", tuple1)
# We can access specific elements of your tuple with the help of indices, just
# like we did with lists. So Here I want to display the element at Index2 in
# my variable tuple1
print("At index 2 in tuple 1 is:", tuple1[2])
print("")
# We can use the range() method we saw for lists with tuples as well. Of course
# we have to cast the generator range() to the corresponding data structure
# using the tuple() method
tuple2 = tuple(range(6))
print("This is tuple2:", tuple2)
print("tuple2 is of type:", type(tuple2))
print("")
# If you want to create a tuple with just one entry, you ALWAYS have to add a
# comma after your element inside the brackets. If your forget this, you will
# NOT create a variable of the type tuple but of the type of your element.
# Python is not able to read this as a tuple otherwise.
tuple3 = ("Christoph",)
print("This is tuple3:", tuple3)
print("tuple3 is of type:", type(tuple3))
