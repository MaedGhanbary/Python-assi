name= input("Enter Name: ")
family= input("Enter Familiy: ")
a= float(input("Enter a:"))
b= float(input("Enter b:"))
c= float(input("Enter c:"))
Average= (a+b+c)/3
if Average>=17 and Average<=20:
    print("Great")
else:
    if Average<17 and Average>=12:
        print("Normal")
    else:
        if Average<12 and Average>=0:
            print("Fail")
        else:
            print("Enter another numbers: ")
