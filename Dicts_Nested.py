"""
This is the example script for working with nested dictionaries. This small
program shows you how to create these dictionaries and how you can access, the
corresponding values
"""
# First we initialize our dictionary as we learned yesterday. We could put all
# inner Dictionaries directly into the outer one by using the Notation, shown
# in line 10, but since this can lead to very long lines of code, I prefer to
# create an empty dictionary and than put in the data step by step.
# dictionary1 = {"Kathrin": {"Name": "Knorr", "Age": 58, "Employer": "KM"}}
dictionary1 = {}
# After we crated our empty dictionary, we can now add the values for our keys
# Here each key of our outer dictionary is paired with another dictionary that
# contain 3 key value pairs
dictionary1["Christoph"] = {"Name": "Knorr", "Age": 35, "Employer": "CQ"}
dictionary1["Gundolf"] = {"Name": "Stoll", "Age": 60, "Employer": "IBW"}
dictionary1["Bennet"] = {"Name": "Wiegert", "Age": 40, "Employer": "SCM"}
# Now we can print out pur dictionary and specific values.
print("Our dictionary looks like this:\n", dictionary1, "\n")
# To access on of the inner dictionaries we have to use the keys of our outer
# dictionary as shown below
print("The value for the key Bennet looks like this:\n", dictionary1["Bennet"])
# Last but not least to access a specific value inside our inner dictionaries
# we have to use two keys in a row. So below we access the value of the key
# Employer from the dictionary that is the value of the key Bennet. You always
# have to use the right order, that means first the key of the outer dictionary
# than the key of the inner dictionary and so on...
print("\nThe Employer of Bennet is:", dictionary1["Bennet"]["Employer"])
