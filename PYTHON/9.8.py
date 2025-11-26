#9.8
STACK=[]
while True:
    print()
    print("1. PUSH()")
    print("2. POP()")
    print("3. EXIT")
    print()
    choice=int(input("USER'S CHOICE: "))
    if choice==1:
        pin=int(input("Pin code of a city, "))
        name=input("Name of city.")
        STACK.append([pin,name])
    elif choice==2:
        if STACK!=[]:
            STACK.pop()
        else:
            print("Underflow")
    elif choice==3:
        print("EXITED BY USER")
        break
    print(STACK)