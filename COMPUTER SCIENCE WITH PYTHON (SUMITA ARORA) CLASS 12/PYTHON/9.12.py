#9.12
Arr=[]
def INSERT(Arr,data):
    Arr.append(data)
def DELETE(Arr):
    Arr.pop(0)
while True:
    print()
    print("1. INSERT(Arr,data)")
    print("2. DELETE(Arr)")
    print("3. EXIT")
    print()
    choice=int(input("USER'S CHOICE:"))
    if choice==1:
        data=input("Enter data:")
        INSERT(Arr,data)
    elif choice==2:
        if Arr!=[]:
            DELETE(Arr)
        else:
            print("Underflow")
    elif choice==3:
        print("EXITED BY USER")
        break
    print(Arr)