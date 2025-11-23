#6.2
def product(a,b):
    if b==0:
        return 0
    if b<0:
        return -product(a,-b)
    return a+product(a,b-1)
a=int(input("Enter first number: "))
b=int(input("Enter second number: "))
print("Product:",product(a,b))