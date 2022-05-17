"""
This is the example I created when discussing how to handle group exercise2
I won't comment on it since, all of you should have a running and more complex
version of it in your directories.
"""
number1 = int(input("Number1: "))
number2 = int(input("Number2: "))
number3 = int(input("Number3: "))
number4 = int(input("Number4: "))

print("Choose 1 for Addition")
print("Choose 2 for Subtraction")
print("Choose 3 for Division")

choice = int(input("What operation do you want to run? "))

if choice == 1:
    result1 = number1 + number2
    result2 = number3 + number4
    print("The addition result is ...")
elif choice == 2:
    result2 = number1 - number2
elif choice == 3:
    result3 = number1/number2/number3/number4
else:
    print("Wrong choice")
