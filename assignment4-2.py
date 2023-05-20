import math
while True :
    introduction = input("Hi, as you know I can solve the Quadratic Equation in form ((ax2)+bx+c=0),Choose Start and Enter information or choose Exite: ")
    if introduction == "Exite" or introduction == "exite":
        break
    if introduction == "Start" or introduction == "start" :
        a = float(input("Enter a: "))
        b = float(input("Enter b: "))
        c = float(input("Enter c: "))
        delta = ((b*b)-(4*a*c))
        
        if delta < 0 :
            print("question doesn't have any answer")
        else:
            sdelta = math.sqrt(delta)
            
            def soluthion1():
                x1 = (((-1*(b))-sdelta)/2*(a))
            
                print("First answer of X: ",x1)
            soluthion1()
            def soluthion2():
                x2 = (((-1*(b))+sdelta)/2*(a))
                print("Second answer of X: ",x2)
            soluthion2()
            if delta == 0:
                x = (-1)*b/2*a    
                print("There is one answer for X: ",x)