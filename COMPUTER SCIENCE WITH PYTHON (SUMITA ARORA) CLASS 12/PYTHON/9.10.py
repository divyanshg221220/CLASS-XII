#9.10
Stack=[]
def PUSH(Books):
    Stack.append(Books)
def POP(Books):
    Stack.pop(Stack.index(Books))
while True:
    print()
    print("1. PUSH(Books)")
    print("2. POP(Books)")
    print("3. EXIT")
    print()
    choice=int(input("USER'S CHOICE: "))
    if choice==1:
        Books=input("Enter a book: ")
        PUSH(Books)
    elif choice==2:
        if Stack!=[]:
            Books=input("Enter a book: ")
            if Books in Stack:
                POP(Books)
            else:
                print("Book not found")
        else:
            print("Underflow")
    elif choice==3:
        print("EXITED BY USER")
        break
    print(Stack)