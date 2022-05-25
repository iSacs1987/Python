"""
This is the first of two script for working with the module pickle. This module
allows us to save our variables inside of a file, but we can't read this file
without the module pickle. Here we see how to read in the file later on.
"""
# We import our module
import pickle

# Now we can read in our file with the pickle.load method. This method takes
# again our file (this time it has to exist) inside the open method as argument.
# Here we need to specify "rb" for read binary instead of "wb" as we saw before.
# We can assign the values we read out from our file to new variables (here a,b,
# c and d) but you have to specify the exact same number of variables as you
# dumped. That means if you dump 4 variables like we did you also need 4 if you
# read in the file later on.
a, b, c, d = pickle.load(open("Example.pickle", "rb"))
# Now we can print out the values and voila, they are the same as for usePickle1
print(a)
print(b)
print(c)
print(d)
