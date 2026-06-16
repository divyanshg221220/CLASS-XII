#9.14
queue=[]
def AddClient(Client):
    queue.append(Client)
def DeleteClient(Client):
    queue.pop(queue.index(Client))
while True:
    print()
    print("1. AddClient(Client)")
    print("2. DeleteClient(Client)")
    print("3. EXIT")
    print()
    choice=int(input("USER'S CHOICE: "))
    if choice==1:
        Client=input("Enter a client: ")
        AddClient(Client)
    elif choice==2:
        if queue!=[]:
            Client=input("Enter a client: ")
            if Client in queue:
                DeleteClient(Client)
            else:
                print("Client not found")
        else:
            print("Underflow")
    elif choice==3:
        print("EXITED BY USER")
        break
    print(queue)