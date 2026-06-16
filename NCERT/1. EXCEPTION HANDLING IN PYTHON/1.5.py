#1.5
print("Handling exception using try...except...else")
try:
    numerator=50
    denom=int(input("Enter the denominator: "))
    quotient=(numerator/denom)
    print("Division performed successfully")
except ZeroDivisionError:
    print("Denominator as ZERO is not allowed")
except ValueError:
    print("Only INTEGERS should be entered")
else:
   print("The result of division operation is ",quotient)