import random
order = input("Choose between start game and stope: ")
if order == "start game":
    a = random.randint(1,6)
    if a == "6" :
        for i in range(2):
            print(random.randint(1,6))
        
    else:
        print("result: ", a )
if order == "stop" :
    print("Good Bye")