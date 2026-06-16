#1.7
print(" Practicing for try block")
try:
    numerator=50
    denom=int(input("Enter the denominator"))
    quotient=(numerator/denom)
    print("Division performed successfully")
except ZeroDivisionError:
    print("Denominator as ZERO is not allowed")
else:
    print("The result of division operation is ",quotient)
finally:
    print("OVER AND OUT")