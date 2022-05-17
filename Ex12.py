list1 = list(range(20))

print(list1)
input1 = int(input("Give me the start of your slice: "))
input2 = int(input("Give me the end of your slice: "))

if input1 >= len(list1):
    print("Your first number is to big.")
    input1 = int(input("Give me the start of your slice: "))
if input2 >= len(list1):
    print("Your second number is to big.")
    input2 = int(input("Give me the end of your slice: "))

if input1 >= len(list1):
    print("No sclice could be generated")
    print(list1)
elif input2 >= len(list1):
    print("Your end is out of range")
    print(list1[input1::])
else:
    print("Your numbers are good")
    print(list1[input1:input2])
