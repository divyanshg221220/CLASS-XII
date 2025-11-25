#9.6
queue=eval(input("Enter a list: "))
q=int(input("Choose an operation to perform:\n1. push\n2. pop\nEnter your choice (1-2): "))
if q==1:
    n=int(input("Enter a number: "))
    queue.append(n)
elif q==2:
    if queue!=[]:
        queue.pop(0)
    else:
        print("Underflow")
else:
    print("Invalid input")
print(queue)