#9.7
list=[]
while True:
    print()
    print("1. enqueue rear")
    print("2. dequeue front")
    print("3. dequeue rear")
    print("4. EXIT")
    print()
    choice=int(input("USER'S CHOICE: "))
    if choice==1:
        n=int(input("Enter a number: "))
        list.append(n)
    elif choice==2:
        if list!=[]:
            list.pop(0)
        else:
            print("Underflow")
    elif choice==3:
        if list!=[]:
            list.pop()
        else:
            print("Underflow")
    elif choice==4:
        print("EXITED BY USER")
        break
    print(list)