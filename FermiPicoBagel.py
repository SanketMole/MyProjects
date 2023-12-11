import random

ik = int(input("Enter number of digits: "))
a = range(1, 10)
b = (random.sample(a, k=ik))
s = ''
for i in b:
    s += str(i)

first=False
n = int(input("Enter your guess: "))
n1 = str(n)
while (len(n1) != ik):
    print("Enter", ik, "digit number!")
    n = int(input("Enter your guess: "))
    n1 = str(n)
if (n1 == s):
    print("Congratulations! You got first-shot-accuracy")
    for i in range(ik):
        print("Fermi!",end='')
    first=True
else:
    while (n1 != s):
        c = 0
        for i in range(len(s)):
            if (n1[i] == s[i]):
                print("Fermi!", end="")
            elif (s[i] in n1):
                print("Pico", end="")
            else:
                c += 1
        if (c == ik):
            print("Bagel")
        n = int(input("\nEnter your guess: "))
        n1 = str(n)
if (n1 == s):
    if(not first):
        for i in range(ik):
            print("Fermi!",end='')


# for i in b:
#   print(i,end='')