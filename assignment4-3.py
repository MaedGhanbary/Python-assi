n = int(input("Enter your main level of Fbonatchi: "))
def Fibonacci(n): 
    if n<0: 
        print("Unknown number") 
    elif n==0: 
        return 0

    elif n==1: 
        return 1
    else: 
        return Fibonacci(n-1)+Fibonacci(n-2) 

print(Fibonacci(n))