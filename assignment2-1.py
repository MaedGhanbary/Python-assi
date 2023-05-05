import math
while True:
    op = input(" Chooe your action between (+ - * / radical sin cos tan cot factorial) and if you want to stop calculator type exite: ")
    if op == "+":
        num1 = float(input("Enter your number: "))
        num2 = float(input("Enter your second number: "))
        result = num1 + num2

    if op == "-" :
        num1 = float(input("Enter your number: "))
        num2 = float(input("Enter your second number: "))
        result = num1 - num2

    if op == "*" :
        num1 = float(input("Enter your number: "))
        num2 = float(input("Enter your second number: "))
        result = num1 * num2

    if op == "/" :
        num1 = float(input("Enter your number: "))
        num2 = float(input("Enter your second number: "))
        if num2 == 0:
            result = ("Enter your second number again: ")
        else:
            result = num1 / num2

    if op == "radical" :
        a = float(input("Enter your number: "))
        b = float(input("Enter the root order of number: "))
        result = math.pow(a, 1/b)

    if op == "sin" :
        c = float(input("Enter your angle in degree: "))
        result = math.sin(math.radians(c))

    if op == "cos" :
        d = float(input("Enter your angle in degree: "))
        result = math.cos(math.radians(d))

    if op == "tan" :
        e = float(input("Enter your angle in degree: "))
        result = math.tan(math.radians(e))

    if op == "cot" :
        f = float(input("Enter your angle in degree: "))
        result = 1/math.tan(math.radians(f))

    if op == "factorial" :
        g = int(input("Enter your number: "))
        result = math.factorial(g)

    if op == "exite" :
        break
    
    print("result: ", result )