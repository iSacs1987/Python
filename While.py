import random

Ls1 = list(range(100))
random.shuffle(Ls1)

i = 0
while Ls1[i] != 50:
    print("You didn't found the fifty")
    i += 1
    print("You ran",i,"iterations until now")

print("You found the fifty after",i,"iterations")