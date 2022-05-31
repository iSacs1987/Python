"""
This is the example script for reading files in python. I will show you all
three different methods, but I personally would always use the last one to make
sure that I don't use too much memory space. All three methods use the with
statement in combination with the open command and the operator "r" for reading.
"""
# For the first method we open our file inside a with statement
with open("TestFile.txt","r") as read_file:
    # Now we can read our file with the read() method. The whole content of our
    # file is now saved as one string
    contents = read_file.read()
# If we orint out this string, the line breaks are added automatically
print(contents)
print("")
# To show you how the string really looks like I use the repr() method to
# suppress the line breaks
print(repr(contents))
print("")
# For the second method we  again open our file inside a with statement
with open("TestFile.txt","r") as read_file2:
    # Now we use readlines() instead of read() to create a list that contains
    # each line of text as a separate element. So here we get a list with four
    # elements since our file contains four lines
    lines = read_file2.readlines()
# Now we can print out our list to see the strings
print(lines)
print("")
# For the third method we open our file again inside a with statement
with open("TestFile.txt","r") as read_file3:
    # This time we create a generator (for loop) to go through our file line by
    # line. This method only reads in one line at a time inside our memory and
    # thus is the most effective one
    for line in read_file3:
        # Now we can look at each line separatedly and print it out. You will
        # see that we see a line break during the first print command in each
        # iteration as soon as the string contains a newline character (\n) at
        # the end.
        print(line)
        print(repr(line))
        # You can use the strip() method to remove newline characters from your
        # Strings.
        print(line.strip('\n'))
