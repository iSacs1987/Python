"""
This is the example script for working with the module os (operating system). It
allows us to run commands analogous to Linux directly from our Python script
to create or remove directories, to change our current working directory and
even to run external programs directly from our Python script.
"""
# To use this module we have to import it like this
import os

# Now we can start using the different methods which are available to us, with
# the help of the point notation. You have a short description of all these
# command sin my presentation, so I will jus tgive some shor tstatements about
# each line here
# We create a directory called OS, works only if this directory doesn't exist
os.mkdir("OS")
# We create a directory called OS, but this time it works even if it already
# exists
os.makedirs("OS", exist_ok=True)
os.chdir("OS")  # analogous to cd in Linux
print(os.getcwd())  # analogous to pwd in Linux
os.chdir("..")
print(os.getcwd())
# We rename our directory. The first argument is the file or directory we want
# to rename and the second argument is the new Name
os.rename("OS", "New_OS")
os.chdir("New_OS")
print(os.getcwd())
os.chdir("..")
print(os.getcwd())
# We execute the command rmdir New_OS, that means we delete the directory
os.system("rmdir New_OS")
# If we have terminal output from the commands inside os.system we get them in
# our terminal. To use them we have to redirect them into Files (>) and than
# read in the Files later on in our Python script (More about this later)
os.system("cat UseOS.py > NewOutput.txt")
