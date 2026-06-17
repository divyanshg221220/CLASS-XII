#6.4
def sum_sq_digits(x):
    sum=0
    for i in str(x):
        sum+=int(i)**2
    return sum
def ishappy(n):
    sum=sum_sq_digits(n)
    if sum==1:
        syn_sq_digits(1)
    elif len(str(sum))>1:
        ishappy(sum)
    else:
        syn_sq_digits(0)
def syn_sq_digits(q):
    if q:
        print(n,"is a happy number")
    else:
        print(n,"is not a happy number")
n=int(input("Enter a number:"))
ishappy(n)