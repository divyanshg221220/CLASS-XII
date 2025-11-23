#6.1
def prime(n,divisor=2):
    if n<=1:
        return False
    if divisor*divisor>n:
        return True
    if n%divisor==0:
        return False
    return prime(n,divisor+1)
n=int(input("Enter a number : "))
if prime(n):
    print(n,"is prime")
else:
    print(n,"is not prime")