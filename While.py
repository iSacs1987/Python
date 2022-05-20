"""
This is the example script for working with while loops. Here I included two
different while loops to show you different predicates that are available to
you when creating these kind of loops. Please keep in mind that you always need
a predicate, that means a statement that can be either True or False when
working with these loops. Make sure that this statement can be come False at
some point during your iterations, otherwise you have a never-ending loop
"""
# I use an external module called random here so that the number of iterations
# I need at each program start differ. We will talk about external modules in
# general and random in detail later on. So for now just accept the import like
# this
import random

# Now I generate a list with elements from 0 until 99
list1 = list(range(100))
# Since I want to have some kind of randomness I use the shuffle method of the
# module random to mix up my list. As you can see we can use methods from other
# modules with a point notation just like we saw for list methods. More about
# this again when we will talk about modules next week.
random.shuffle(list1)
# No I can create my first while loop, that searches for the number 50 inside
# my randomized list. I need a running index that I have to define beforehand
# unlike with our for loop. So here I choose the variable i as running index
# again. It's an international convention to use i,j,k,l etc. as running indices
# in loops, but you can always use other names as well.
i = 0
# After the definition of my running index I can now start my loop by writing
# down the while (predicate): line I need for it's construction. Here I check
# whether the current element of my randomized list (list1[i]) is not equal (!=)
# to 50. As long this is true, the code below the while statement is executed.
# As soon as this statement becomes False, the loop is terminated right here and
# there, that means the code is NOT executed anymore.
while list1[i] != 50:
    # I just included some print statements inside my loop, to show you how this
    # jumps from value to value
    print("You didn't found the fifty")
    print("You ran", i + 1, "iterations until now")
    # The line below is the most important line for this loop. If we forget to
    # increase our iterator i we will always be stuck at the question
    # list1[0] != 50? and thus we can't terminate our loop. So we have to make
    # sure whenever we use while loops that the condition we set in line 34 can
    # be false after a certain number of iterations.
    i += 1
print("You found the fifty after", i, "iterations")
# In included a second while loop example here, where I don't use my running
# index to create my predicate but the sum I caclulate inside my loop.
i = 0
sum = 0
while sum < 2500:
    sum += list1[i]
    print(f"After {i+1} iterations your still under the Threshold")
    i += 1
print("You reached the Threshshold of:", sum)
