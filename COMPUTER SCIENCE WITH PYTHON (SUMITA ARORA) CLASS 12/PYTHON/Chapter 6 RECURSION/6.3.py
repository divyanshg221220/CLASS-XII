#6.3
def hailstone(n):
    print(int(n))
    if n==1:
        return 1
    if n%2==0:
        hailstone(n/2)
    else:
        hailstone(3*n+1)
n=int(input("Enter a number:"))
hailstone(n)