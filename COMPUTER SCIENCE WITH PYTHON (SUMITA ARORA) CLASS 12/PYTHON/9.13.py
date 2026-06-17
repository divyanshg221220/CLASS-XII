#9.13
Arr=eval(input("Enter a list:"))
stack=[]
def PUSH(Arr):
    for i in Arr:
        if i%5==0:
            stack.append(i)
PUSH(Arr)
if stack!=[]:
    print(stack)
else:
    print("Empty stack")