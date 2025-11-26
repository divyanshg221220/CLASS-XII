#9.11
Queue=[]
def Insert(City):
    Queue.append(City)
def Delete(City):
    Queue.pop(Queue.index(City))
while True:
    print()
    print("1. Insert(City)")
    print("2. Delete(City)")
    print("3. EXIT")
    print()
    choice=int(input("USER'S CHOICE: "))
    if choice==1:
        City=input("Enter a city: ")
        Insert(City)
    elif choice==2:
        if Queue!=[]:
            City=input("Enter a city: ")
            Delete(City)
        else:
            print("Underflow")
    elif choice==3:
        print("EXITED BY USER")
        break
    print(Queue)