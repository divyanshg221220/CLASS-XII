#9.3
def POP(Arr):
    if Arr!=[]:
        return Arr.pop()
    else:
        return "Underflow"
stack=eval(input("Enter a list: "))
print(POP(stack))