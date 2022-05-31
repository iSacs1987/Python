"""
This is the exampel script for writing files. I will show you two ways to write
things into files her
"""
# First I define two variables I will need later on
string1 = "Hello Christoph"
float1 = 456.34
# Now we can use the first method by simply opening the file. We can even use
# files that do NOT exist because the will be created by the open statement. We
# always have to specify an operator as second argument for writing files this
# operator can be either "w" for writing (over writes contents of the file) or
# "a" for appending (adds text to the end of the file)
file = open("TestFile.txt","w")
# Now we can use the .write() method to add text to our file. This method takes
# only strings as argument and writes them to your file. Please keep in mind
# that you have to add line breaks (\n) on your own.
file.write("My name is Christoph\n")
file.write("Hello World\n")
# We can even write the value of our variables into the file
file.write(string1)
# But if the datatype of your variable is something else than string please
# don't forget to cast it to a string.
file.write(str(float1))
# Again you have to add line breaks and spaces on your own.
file.write("\n")
# file.write also accepts f-strings as argument, with the help of this method
# you can write all kind of variables into your files without the need of
# casting them to string
file.write(f"{string1} you're getting paid {float1} Euros")
# After you wrote everything in your file you have to close it. Otherwise the
# changes you made are NOT saved to your hard drive.
file.close()
# The second method uses the with statement, which allows us to work on a file
# as long as we are inside this statement. It is similiar to if statements in
# the way that as long as your code has the same indent everything underneath
# the with statement is seen as part of it. As soon as you return to your main
# program (line 45) your file is closed and saved automatically. This statement
# works again with out open command and an alias for our file (as with_file)
with open("TestFile2.txt","w") as with_file:
    # Now we can write into our file. Again we have to add line breaks on our
    # own. The writing than works just as we saw before.
    with_file.write("This is a test Test\n")
    with_file.write(string1)
    with_file.write(str(float))
