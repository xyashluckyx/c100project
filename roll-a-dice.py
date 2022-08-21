import random
response=str(input("Press y to roll again and n to exit: "))

while response=="y":
    no=random.randint(1,6)
    if(no==1):
        print("[ ----- ]")
        print("[ ----- ]")
        print("[   0   ]")
        print("[ ----- ]")
        print("[ ----- ]")

    elif(no==2):
        print("[ ----- ]")
        print("[ ----- ]")
        print("[0     0]")
        print("[ ----- ]")
        print("[ ----- ]")

    elif(no==3):
        print("[ ----- ]")
        print("[ ----- ]")
        print("[0  0  0]")
        print("[ ----- ]")
        print("[ ----- ]")

    elif(no==4):
        print("[ ----- ]")
        print("[ 0   0 ]")
        print("[       ]")
        print("[ 0   0 ]")
        print("[ ----- ]")
    elif(no==5):
        print("[ ----- ]")
        print("[ 0   0 ]")
        print("[   0   ]")
        print("[ 0   0 ]")
        print("[ ----- ]")
    response=str(input("Press y to roll again and n to exit: "))
response=="n"

