#1.2
print("Practicing for try block")
try:
    numerator=50
    denom=int(input("Enter the denominator"))
    quotient=(numerator/denom)
    print(quotient)
    print("Division performed successfully")
except ZeroDivisionError:
    print("Denominator as ZERO.... not allowed")
print("OUTSIDE try..except block")