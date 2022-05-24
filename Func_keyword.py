"""
This is the example script for working with keyword arguments in functions. It
shows you how you can change the order of the arguments you hand over to your
funtions
"""
# First we have to define our function. This is the same function I used
# yesterday to explain the usage of default arguemtns to you.
def greeting(Name, msg="Good Morning!"):
    print("Hello", Name + ", " + msg)


# Now we can generate our call backs. The first one hands over the arguments
# with the keywords (Name= and msg=) in the order our signature dictates.
greeting(Name="Christoph", msg="How do you do?")
# The second one changes the order of our arguments, with msg being now the
# first one and Name the second on. Still the call back works.
greeting(msg="How do you do?", Name="Christoph")
# The third one uses only one keyword for msg and hands over the argument Name
# normally. Please keep in mind that than using this combination you still have
# to stay true to the order in your signature. That means you have to have the
# values of your positional arguments at the beginning of your call back and
# than add the arguments with keywords.
greeting("Christoph", msg="How do you do?")
# That's why the example below won't work here. Even though we use the keyword
# for msg, we will get an error message since our positional argument Name is
# not at the position, Pythone xpects it to be.
# greeting(msg="How do you do?","Christoph")
