import random
n = int(input("How many number do you want in your array? "))
n1 = int(input("How far is your range? (1,...): "))
a = []


while len(a) != n :
    b = a.append(random.randint(1,n1))
    if a.count(b) == 1 :
        break

print(a)