#1.4
print("Handling exceptions without naming them")
try:
    numerator=50
    denom=int(input("Enter the denominator"))
    quotient=(numerator/denom)
    print("Division performed successfully")
except ValueError:
    print("Only INTEGERS should be entered")
except:
    print(" OOPS.....SOME EXCEPTION RAISED")