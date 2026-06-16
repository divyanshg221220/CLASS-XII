#1.3
print("Handling multiple exceptions")
try:
    numerator=50
    denom=int(input("Enter the denominator: "))
    print(numerator/denom)
    print("Division performed successfully")
except ZeroDivisionError:
    print("Denominator as ZERO is not allowed")
except ValueError:
    print("Only INTEGERS should be entered")