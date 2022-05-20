"""
This program shows you how you can create multi-dimensional lists and how to
access specific values inside of them.
"""
# We have three ways to create multi-dimensional lists. The first one is by
# simply using [[],[]] and writing the elements inside our brackets
matrix1 = [[0, 1, 2], [0, 1, 2], [0, 1, 2]]
# The second one is by using list(range(X)) multiple times inside of []
matrix2 = [list(range(5)), list(range(5))]
# And last but not least we can use the method below, but as we saw this is
# pretty problematic since all sublists point at the same place in the memory
# and thus if you make a changes to one of the sublists all of them are changed
matrix3 = [list(range(4))] * 8
# So now we can print out our multi-dimensional lists.
print(matrix1)
print("")
print(matrix2)
print("")
print(matrix3)
print("")
# If we use the method of line 13 but include the multiplication in the square
# bracket we get something different. Please don't ask me whythis happens, I
# just know that it happens.
print([list(range(6)) * 5])
print("")
# If we want to access specific elements in our multi-dimensional lists we have
# to use multiple indices. The two lines below show the logic behind this. The
# first index specifies the corresponding sublist, for matrix1 it can be 0, 1 or
# 2. The second index specifies than the position in this sublist. Please keep
# in mind that sublist1 here is just an example name I use to visualize the
# logic behind multiple indices and NOT a correct variable name.
# matrix1[1] ==> [0,1,2] ==> sublist1
# matrix1[1][0] ==> sublist1[0] ==> 0
matrix1[1][0] = 15  # We change the first element of the second sublist to 15
matrix2[0][4] = 100  # We change the fifth element of the first sublist to 100
matrix3[6][1] = 25  # We change the second element of the seventh sublist to 25
# If we now print out our multi-dimensional lists again. We can see the changes
print(matrix1)
print("")
print(matrix2)
print("")
print(matrix3)
# As you saw for matrix3 all 1's in the 8 sublists were replaced with a 25,
# since they all point at the same place in the memory.
