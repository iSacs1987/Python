"""
This is the example script that shows you how to use dictionaries in Python.
Please keep in mind that in dictionaries each value is associated with a key.
The line 9 and hte lines 10 to 13 produce the same dictionary1. These are the
two different methods to initalize a dictionary, either by directly handing over
the key value pairs (line 9) or by intializing an empty dictionary first and
than add the corresponding key-value-pairs step by step.
"""
# dictionary1 = {"Hello": "World", "3+4": 7, "5/2": 2.5}
dictionary1 = {}  # Initalize the empty dictionary
dictionary1["Hello"] = "World"  # Add the value "World" to the key "Hello"
dictionary1["3+4"] = 7  # Add the value 7 to the key "3+4"
dictionary1["5/2"] = 2.5  # Add the value 2.5 to the key "5/2"
print("Our dictionary looks like this:\n", dictionary1)
print("")
# We can also use numbers as keys, but it's better to use strings that are more
# descriptive as keys. So even though the example below works, please try to
# NOT use numbers as keys
dictionary1[9] = "Bye"
print("Our dictionary looks like this:\n", dictionary1)
print("")
# If we want to access the data in our dictionary we have to use the key to get
# to the corresponding value. So in the example below we want to get the value
# "World", which is associated with the key "Hello". So we now can use something
# that looks similar to accessing entries in our lists, since we are also using
# the square brackets [] but this time we have to write the corresponding key
# (a string) into them and NOT an index (a number)
print("The value for the key 'Hello' is:", dictionary1["Hello"])
print("")
# Here we add another key-value-pair to our dicitionary, which is a duplicate
# since originally this program created the dictionary just with line 9 ;)
dictionary1["9-3"] = 6
print("Our dictionary looks like this:\n", dictionary1)
# If we add data to our dictionary by using an already existing key (in our case
# "Hello"), than the associated value inside our dictionary is replaced. So you
# have to always be careful than adding data to your dictionary, so that you
# don't replace things you need later on.
dictionary1["Hello"] = "Hi"
print("Our dictionary looks like this:\n", dictionary1)
print("")
# The del command allows us to delete key-value-pairs from our dictionary. By
# using the code below we tell Python ok delete the key-value-pair of the key
# "3+4" and the value 7
del dictionary1["3+4"]
print("Our dictionary looks like this:\n", dictionary1)
print("")
# We can look for specific keys in our dictionary in a matter that is again
# similar to lists. The if statement below asks if dictionary1 has a key called
# "Hello", which is the case here.
if "Hello" in dictionary1:
    print("Hey you know which keys you used for your dictionary\n")
else:
    print("You don't know the keys of your own dictionary?\n")
# Of course the reverse is also true. So now we ask if dictionary1 has NO key
# called "Hi", which again is true for our case, since "Hi" is only a value
# associated with the key "Hello"
if "Hi" not in dictionary1:
    print("Hey you know which keys you used for your dictionary\n")
else:
    print("You don't know the keys of your own dictionary?\n")
# A last thing I want to show you, while working with dictionaries are the
# methods keys() and values(). These are dictionary methods and can be used
# witht he help of the point notation, as we saw for append or insert when
# working with lists. They allow you to generate a list of either all keys
# (lines 69 and 71) or all values (lines 70 and 72), but these lists are NOT
# sorted. Similar to range() these methods return not a list but a so called
# dict-keys or dict-values object. So we have to cast these to lists as shown in
# lines 71 and 72.
print("Our dict-keys object looks like this:", dictionary1.keys())
print("Our dict-valuess object looks like this:", dictionary1.values())
print("Our list of keys looks like this:", list(dictionary1.keys()))
print("Our list of values looks like this:", list(dictionary1.values()))
