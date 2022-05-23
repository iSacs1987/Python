"""
This is the example script for working with default arguments. This is a new way
to create function signatures
"""
# We can create functions wwith default parameters by using assignments inside
# our signature. So in the example below Name is a positional argument you
# always need during the call back, whereas msg is an optional argument you can
# skip during the call back. If you skip the argument msg, the value given in
# the signature "Good Morning!" is taken instead. You always have to keep in
# mind that you have to write down all positional arguments first, before you
# can add arguments with default values to your signature. That means if you
# have a function witht he positional arguments Name, Date and Age and default
# values for the argument msg, xour signature has to look similair to this:
# def function_name(Name, Date, Age, msg=Default_Value):
def greeting(Name, msg="Good Morning!"):
    print("Hello", Name + ", " + msg)


# The call back for our function now can look like this. We just hand over the
# needed positional argument Name (Kate) and skip the argument with default
# values msg.
greeting("Kate")
# On the other hand we can also create a call back with two arguments. Again the
# first one has to be our positional argument Name, and the second one is our
# optional argument msg. When the function is now executed the default value of
# msg is over written with the handed over value inside our call back. That
# means instead of "Good Morning!", the print out now contains "How do you do?"
greeting("Bruce", "How do you do?")
# Please keep in mind that when using multiple positional and optional arguments
# that the order is essential. That means you always have to hand over all
# needed positional arguments before the optional ones. If you want to only
# change the value of one of your optional arguments, which is not the first one
# than you run into problems. There is a method to do this though by using
# keywords, which we will talk about a bit later.
