#9.15
Stack=[]
def Addnew(Book):
    Stack.append(Book)
def Remove(Book):
    Stack.pop(Stack.index(Book))
while True:
    print()
    print("1. Addnew(Book)")
    print("2. Remove(Book)")
    print("3. EXIT")
    print()
    choice=int(input("USER'S CHOICE: "))
    if choice==1:
        Book=input("Enter a book: ")
        Addnew(Book)
    elif choice==2:
        if Stack!=[]:
            Book=input("Enter a book: ")
            if Book in Stack:
                Remove(Book)
            else:
                print("Book not found")
        else:
            print("Underflow")
    elif choice==3:
        print("EXITED BY USER")
        break
    print(Stack)