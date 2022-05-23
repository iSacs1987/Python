"""
This is the example script I created to explain the usage and strength of while
loops to you.
"""
# I import the module random here, to use it later for mixing up, my list. Just
# ignore it for now, we will talk about the usage of modules later
import random

# In my first example I show you a way to torture your user, to give you a
# specific input. Therefore we have to deifne a variable number that takes an
# input from the user and cast it directly to an integer
number = int(input("Please type in a number: "))
# Let's say the user typed in 5 here. Now we have to start our loop by using the
# while operator and creating our predicate. For this example we want the user
# to type in the number 8, so that means we want him to repeat his inputs as
# long as he didn't type in the right number. So We have to ask the question if
# the number handed over from the user is NOT 8 in this case. Please remember
# we have to create a predicate that can be True or False and as long as the
# predicate stays True our loop is repeated. Therefore we compare the input from
# the user (number) with the number 8 and we have to use the not equal (!=)
# operator here
while number != 8:
    # For this Example our predicate is True for the firs input since 5 is not
    # equal to 8. Now the whole code block that is associated with our while
    # loop is executed. That means we get the print out and than the user has
    # to type in something again.
    print("Wrong choice")
    # Now the user is asked to type in something again. Let's say he types in 7
    # for this first iteration, now we jump back to line 21 and ask again
    # whether our input is equal to 8 or not. If the predicate is still True,
    # the code inside the loop will be executed again. This repeats as long as
    # the user, doesn't type in 8. As soon as number is assigned the value 8 by
    # the user, the program will still go back to line 21, but now the predicate
    # returns False and the loop is stopped. The program than jumps to line 36
    # and continues from there on.
    number = int(input("Try again: "))
# For my second example I choose something that is similiar to running recursive
# calculations, even though the example is very simple. So I define my control
# variable called sum1 to have a value of 1.
sum1 = 1
# Now I can create my while loop in combination with a predicate. Here in this
# case I ask the question if my control variable (or running index or loop
# variable or iterator) has a value that is less than 1000. As long this
# question returns True as answer the code in lines 50 and 64 is repeated.
while sum1 < 1000:
    # During each of my iterations I simply double the value of sum1 by adding
    # it to itself. Please remember that sum1 += 1 is the same as
    # sum1 = sum1 + sum1. So we start with a value of 1 for sum1 and than the
    # value increases in the following manner: 1, 2, 4, 8, 16, 32,...,512, 1024
    sum1 += sum1
    # I included a print out here to show you on the one hand how sum1 increases
    # it's value and on the other hand to give you an example for testing if
    # your loops functions correctly or not. When creating such loops please
    # try to inlcude simple print statements to check whether your loop reaches
    # an end or not. If you don't have any kind ou output in your terminal you
    # won't know if you have an indefinite loop or if the calculation just takes
    # very long. This process is called print-debugging and is one of the ways
    # to search for semantics errors in your programs. This is especially useful
    # when working with while loops. Here in this example we could run into an
    # indefinite loop if we would have defined sum1 with a value of 0 in line 40
    # for example. Since we would just add up zeros in line 50 we never would
    # reach a value that returns False for pur predicate in line 45. So please
    # be careful when working this these kind of loops.
    print(sum1)
# The third example shows you that you could always use for loops when working
# with lists instead of using while loops. I personally prefer to use for loops
# when working with lists, since in most cases its more logical and easier to
# use them. For this example I generate a list that contains values from 0 up
# to 100 by simply using the range method.
list1 = list(range(101))
# Now I mix the list at random, so that I don't know the index of number 50. We
# will talk about the module random and its functions later on, so for now just
# ignore this line here.
random.shuffle(list1)
# The set up for working with a while loop in combination with lists is a bit
# different from what we saw before. First we have to define our control
# variable by ourselves. Since in contrast to for loops where this is done
# automatically we have to do it manually here. I choose to use the simple
# iterator i we saw when we were working with for loops. So I define i here and
# assign it the value 0, so that I can use it as an index for my list
i = 0
# Now I can create my while loop, by using a predicate that asks whether the
# current number (list1[i]) is NOT equal to 50. As long as this statement is
# True my loop will repeat the corresponding code.
while list1[i] != 50:
    # I included a simple print statement to show you the progress of the loop.
    # This time I used a f-string that allows me to combine strings with
    # variables. We learned how to use them in the beginning of our Python
    # course. The f before the quotes (") indicates that we use a f-string and
    # than everytime we encounter {} with a variable inside the variable is
    # replaced by its value.
    print(f"We are in iteration {i+1} and 50 wasn't found yet")
    # Now I have to include the most important line of this whole loop, the
    # update of our control variable. If I forget this line our loop would run
    # indefinitely because we would always compare list1[0] with the number 50
    # and wouldn't go to the next entry in our list. That's why we have to make
    # sure the value of the iterator i is increased in each repition of our loop
    i += 1
# This for loop does the same as the while loop we saw above. This time we loop
# through our list with a for each loop.
for elem in list1:
    # Now we have to create an if statement, that checks whether we encountered
    # a value NOT equal to 50 or not. So thats why we use the if elem != 50, to
    # reproduce the behavior of our while loop here.
    if elem != 50:
        # Now we have a simple print out to mimic the print out we included in
        # the while loop. The statement below will be executed every time the
        # element of our list is NOT equal to 50.
        print("We didn't find the fifty yet")
    # To be able to stop our loop as soon as we encounter the 50, we have to
    # use an else statement here. Otherwise, we just would skip the print out in
    # line 109, one time, and than go on with this loop until we reach the end
    # of our list
    else:
        # To stop the loop we can use the keyword break, which tells Python to
        # stop the current loop and resume with the code outside of our loop.
        # That means the break statement here tell Python to jump to line 120
        # and go on with the normal code afterwards.
        break
# I just included a small print Statement at the end of the program to show you
# the usage of break here.
print("The End")
