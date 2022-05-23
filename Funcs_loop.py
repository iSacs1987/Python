"""
This is the example program for including loops inside of your functions. The
general principles for working with functions remain as we saw beforehand.
"""
# First we have to create the signature of our function. I named the parameter
# inputlist, so that I know that I have to hand over some kind of iterable on
# the call back of my function later on.
def sum_over(inputlist):
    # Again I have to define my local variable result, so that I can return the
    # corresponding result later on.
    result = 0
    # Now I can create my loop by iterating over all elements of the handed over
    # iterable (inputlist). Please keep in mind that this is just a temporary
    # name which is only available during the execution of your function, since
    # again this is a local variable.
    for elem in inputlist:
        # Now I have the code which should be repeated during the execution of
        # my function, in our case simple adding up the values of my list.
        result += elem
    # To make sure that I can work with the calculated result, I have to use a
    # return statement again. Please make sure, that this statement is inside
    # of your function but outside of your loop. This is done by using different
    # indentations. The general code that is executed inside our function has an
    # indentation of one tabstop, while the code that is executed during our
    # loop has an indentation of two tabstops here. So please always be careful
    # with your indentations.
    return result


# Now I define two different lists, with the help of the range method, as we saw
# multiple times already.
list1 = list(range(10))
list2 = list(range(15))
# Now I can call back my function sum_over with the help of these lists. Please
# keep in mind that a call back like this: sum3 = sum_over(5) would return a
# syntax error, since you didn't hand over an iterable but a simple integer. So
# always keep in mind which kind of datatype (or type of data structure) your
# functions expect from you during the call back.
sum1 = sum_over(list1)
sum2 = sum_over(list2)
# last but not least I can print out the results of our call backs.
print(sum1)
print(sum2)
