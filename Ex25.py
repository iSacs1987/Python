max = 0
maxi = 0
maxj = 0
float1 = 2.4
string1 = "Hello"
bool1 = True
print(max)
new_max = max + 3


max = 9
print(max)
max = max + 3
string1 = 10
max += 1  # ==> max = max +1

if max > 0:  # Returns True
    division = float1 / max
    print(division)
elif max < 0:
    multiplication = float1 * max
    print(multiplication)
else:
    print("Wrong Number")

string1 = "World"

sum = 50 + 65
if sum > 100:
    print(sum)
elif sum > 10:
    print(sum, "Hello")
elif sum > 1:
    print(sum, "World")

list1 = [4, 0, 1, 2, 3]
list2 = []
range1 = range(10)
list3 = list(range(10))  # range(10) ==> (0,1,2,3,4,5,6,7,8,9)
# list3 ==> [0,1,2,3,4,5,6,7,8,9]
print(range1)
length1 = len(list1)  # ==> length1 is assigned the value 4


print(list1[1])
check1 = 5

if check1 in list1:  # ==> if 5 in list1
    print("You found the 5")
if check1 not in list1:
    print("5 is not part of list1")

print(list3[2:6])  # start_index:end_index ==> [2,3,4,5,6]
print(list1[:2])  # ==> first 2 elements
print(list1[1:])  # ==> everything starting at index 1 ==> exclude first element

# Name_of_element.method(arguments) ==> point notation
# list1: [4,0,1,2,3]
list1.append(20)  # ==> Add an element to the end of list1 ==> we add 20 to list1
# ==> list1 : [4,0,1,2,3,20]
list1.extend(list3)  # Works only with iterables ==> only with lists, tuple etc.
# ==> extend takes each element of list3 and adds it as new element to list1
# ==> list3: [0,1,2,3,4,5,6,7,8,9]
# ==> list1: [4,0,1,2,3,20,0,1,2,3,4,5,6,7,8,9]
list1.sort()
# ==> list1: [0,0,1,1,2,2,3,3,4,4,5,6,7,8,9,20]
list1.reverse()
# ==> list1: [20,9,8,7,6,5,4,4,3,3,2,2,1,1,0,0]
list1.insert(5, 25)
# ==> list1: [20,9,8,7,6,25,5,4,4,3,3,2,2,1,1,0,0]

dictionary1 = {}
dictionary1["Name"] = "Christoph"
dictionary1["Age"] = 35
dictionary2 = {"Name": "Gundolf", "Age": 60}
# ==> "Name" and "Age" are keys
# ==> "Christoph" and 35 or "Gundolf" and 60 are the corresponding values
# ==> Pairs: "Name" and "Christoph", "Age" and 35
print(dictionary2["Age"])  # returns 60
dictionary2["Age"] = 61
print(dictionary2["Age"])  # returns 61

dictionary3 = {}
dictionary3["Bennet"] = {"Name": "Wiegert", "Age": 40, "Employer": "SCM"}
# ==> instead of having an int or string as Value we now have a dictionary
# as value
print(dictionary3["Bennet"]["Name"])  # returns "Wiegert"
# print(dictionary3["Name"]["Bennet"]) # returns a Key-Error

keys1 = list(dictionary1.keys())
# ==> returns an ordered list of the keys of our dictionary1 (Python 3.7 up)
# ==> keys1: ["Name","Age"]
values1 = list(dictionary1.values())
# ==> values1: ["Christoph",35]

tuple1 = ("Hello", "World", "How")
tuple2 = ("Christoph",)

set1 = {4, 5, 6, 7, 7, 2}
set2 = {}  # ==> creates an empty dictionary
set3 = {
    5,
}

# Main usage of sets
# list1: [20,9,8,7,6,25,5,4,4,3,3,2,2,1,1,0,0]
list1 = list(set(list1))  # ==> sets don't allow duplicates
# works from inside to outside:
# 1. list1 is changed to type set
# 2. list1 (now of type set) is changed to type list
# list1: [20,9,8,7,6,25,5,4,3,2,1,0]

matrix = [[1, 2, 3], [1, 5, 3, 7], [1, 2, 3, 10, 4]]
# matrix has 3 elements and each element is a sublist
# sublists: [1,2,3] & [1,5,3,7] & [1,2,3,10,4]
print(matrix[1][2])  # returns 3
# ==> matrix[1] ==> sublist1 ==> [1,5,3,7]
# ==> matrix[1][2] ==> sublist1[2] ==> [1,5,3,7][2] ==> 3

sum1 = 0  # simple variable Assignment
# We need for loops:
# 1. an iterator or loop variable or running index ==> i
# 2. an iterable, eg. list, set, tuple, range ...
# range(10) ==> (0,1,2,3,4,5,6,7,8,9)
for i in range(10):
    # we assign the values from our iterable (range) to i and change it's value
    # accordingly. i starts with a value of 0 and than goes to 1 to 2 etc..
    # until it reaches value 9
    sum1 += i
    print(i)
    print(sum1)

# Of course we can use if-clauses in our loops as well
# Of course we can use ranges like this as well:
# range(X) ==> 0,1,2,...,X
# range(X,Y) ==> X,X+1,X+2,....,Y
# range(X,Y,Z) ==> X, X+Z, X+2*Z,....,Y

print(sum1)

i = 0
sum1 = sum1 + i  # 0 + 0
print(i)
print(sum1)
i = 1
sum1 = sum1 + i  # 0 + 1 ==> sum1 = 1
i = 2
sum1 = sum1 + i  # 1 + 2 ==> sum1 = 3
i = 3
sum1 = sum1 + i  # 3 + 4
# ...
i = 9
sum1 = sum1 + i  # 46 + 9 ==> sum1 = 55

# list1: [20,9,8,7,6,25,5,4,3,2,1,0]
for number in list1:
    print(number)  # ==> prints out 20 than 9 than 8 etc until 0
print("Finished")

# let's say we don't know the length of list1
# 1. we get the length of our list, the number of elements in it (len(list1))
# 2. Since len(list1) is just a number we can hand over to our range method
# Let's say list1 contains 15 Elements that means range(len(list1)) returns:
# (0,1,2,3,4,5,6,7,8,9,10,11,12,13,14)
for i in range(len(list1)):
    print(list1[i])

matrix = [[1, 2, 3], [1, 5, 3, 7], [1, 2, 3, 10, 4]]

for i in range(len(matrix)):  # we get a range that looks like this (0,1,2)
    # for i = 0: range(len(matrix[i])) returns (0,1,2)
    # for i = 1: range(len(matrix[i])) returns (0,1,2,3)
    # for i = 2: range(len(matrix[i])) returns (0,1,2,3,4)
    for j in range(len(matrix[i])):
        print(matrix[i][j])

for sublist in matrix:  # ==> sublist is 1. [1,2,3], 2. [1,5,3,7] etc.
    # for [1,2,3] ==> number is first 1 than 2 than 3
    # for [1,5,3,7] ==> number is first 1 than 5 than 3 than 7
    # etc...
    for number in sublist:
        print(number)
