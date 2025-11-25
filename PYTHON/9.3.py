#9.3
def POP(Arr):
    if Arr!=[]:
        return Arr.pop()
    else:
        return "Underflow"
list=eval(input("Enter a list: "))
print(POP(list))