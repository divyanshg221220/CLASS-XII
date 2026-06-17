#9.6
queue=[]
while True:
    print()
    print("1. enqueue")
    print("2. dequeue")
    print("3. EXIT")
    print()
    choice=int(input("USER'S CHOICE:"))
    if choice==1:
        n=int(input("Enter a number:"))
        queue.append(n)
    elif choice==2:
        if queue!=[]:
            queue.pop(0)
        else:
            print("Underflow")
    elif choice==3:
        print("EXITED BY USER")
        break
    print(queue)