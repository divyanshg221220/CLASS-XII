#9.1
stack=eval(input("Enter a list: "))
q=int(input("Choose an operation to perform:\n1. push\n2. pop\nEnter your choice (1-2): "))
if q==1:
    n=int(input("Enter a number"))
    stack.append(n)
elif q==2:
    stack.pop()
else:
    print("Invalid input")
print(stack)