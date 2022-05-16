"""
This is the program Printing.py in which I show you how to assign and declare
Variables and how to use the print command to display them in the terminal.
Furthermore this program contains some more complex print commands using commas
and f-strings. This text here at the beginning is a multi line comment as I
discussed on Friday. All other comments will be done by using the #
"""
# First we declare some variables. Pleas stick to the naming conventions I
# explained in the presentation (all lowercase, explicit names using _ for
# separating words). First we declare 3 String variables. Keep in mind that you
# have to use quotation marks "" or '' to tell python that this is a string.
test_var1 = "Hello"
test_var2 = "World"
test_var3 = "Christoph Knorr"
# You saw that I can declare and assign variables in Python without specifing
# the variable type (int, float or string), while this makes our life easier
# when we assign our variables it can create also problems later on if we aren't
# careful. Because we can overwrite all variables at each time and even change
# the type. So if we would later declare something like test_var1 = 5, our
# string variable is now an integer variable. While the declaration itself
# doesn't produce any error it can lead to errors later on. So be careful at
# using variables and make sure that you always know which variable has which
# type. Down below i now declare an integer and a floating point variable, we
# don't need quotation marks here, since we are working with numbers.
age = 35
pay_per_day = 200.45
# On Friday we saw how to print out simple strings, but we can use print also
# to display the value of a variable, simply by using a command as it's shown
# down below. So by putting the variable name (without quotation marks) inside
# the print command we can display the value of our variable in the terminal.
print(test_var3)
print(age)
print(pay_per_day)
# If you include the variable name inside of quotation marks, than python
# interprets it as a string and writes out the corresponding string
print("pay_per_day")
# As mentioned above, we can combine strings with our variables by using either
# commas as shown below or f-strings (a bit mor about tham later). When using
# commas you can combine strings with variables. Each comma is replaced with a
# space during the print out. So the result of the line below is:
# My name is Christoph Knorr and I'm 35
print("My name is",test_var3,"and I'm",age)
# The last way to combine strings with variables are the so-called f-strings.
# By putting a lower case f at the beginning of your print command followed by
# the string you want to print out, we can add variables to our strings at
# different positions. To print out the value of a variable we have to write
# the name of our variable inside of curly brackets {}. Now the value of our
# variable is printed out at the corresponding position. Keep in mind that no
# spaces are added to your print out, while using this method. You can also add
# strings between your variables as shown here with the and between test_var1
# and test_var2
print(f"Learning programming starts with {test_var1} and {test_var2}")
