#9.2
stack=[]
list=input("Enter a string:").split()
for i in list:
    stack.append(i)
for i in stack[::-1]:
    print(i*2,end=" ")