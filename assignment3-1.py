import random

a = input("Choose start or stop: ")
n = 0
if a == "stop" :
    print("Good bye!")
else:
    pc_num = random.randint(1, 20)
    
    while True :
        user_num = int(input("Gess number between (1,20): "))
        n = n+1
        if pc_num == user_num :
            print("Yay, You have won XD")
            print(n , "Times")
            break
        if pc_num > user_num :
            print("Gess more than before")

        if user_num > pc_num :
            print("Gess less than before")

