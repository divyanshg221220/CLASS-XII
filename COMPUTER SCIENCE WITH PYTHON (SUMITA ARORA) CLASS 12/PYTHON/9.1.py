#9.1
stack=[]
while True:
    print()
    print("1. push")
    print("2. pop")
    print("3. EXIT")
    print()
    choice=int(input("USER'S CHOICE:"))
    if choice==1:
        n=int(input("Enter a number:"))
        stack.append(n)
    elif choice==2:
        if stack!=[]:
            stack.pop()
        else:
            print("Underflow")
    elif choice==3:
        print("EXITED BY USER")
        break
    print(stack)