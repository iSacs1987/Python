"""
This is the first of two script for working with the module pickle. This module
allows us to save our variables inside of a file, but we can't read this file
without the module pickle. Here we see how to create the file.
"""
# I import two modules here, which can be done by comma separating them.
import pickle, random

# Now I create some random numbers
random_number1 = random.randint(0, 100)
random_number2 = random.random()
random_number3 = random.gauss(1, 5)
random_list1 = list(range(random.randint(0, 100)))
random.shuffle(random_list1)
# I print our these random numbers
print("Generated by randint:", random_number1)
print("Generated by random:", random_number2)
print("Generated by gauss:", random_number3)
print("Random list:\n", random_list1)
# Now I can save my variables to a file with the dump method of the pickle
# module. pickle.dump takes a tuple which contains our variable names as first
# argument, than we have to hand over the file. This is done with the open()
# method, we will learn more about this later on. open takes a file name (even a
# non existing one, which is than created) and a second argument that tells it
# what to do with this file. Here we use "wb" which stand for write binary. For
# now just keep in mind to use pickle.dump with "wb".
pickle.dump(
    (random_number1, random_number2, random_number3, random_list1),
    open("Example.pickle", "wb"),
)
