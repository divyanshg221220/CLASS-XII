#1.1
print("use of assert statement")
def negativecheck(number):
    assert(number>=0),"OOPS... Negative Number"
    print(number*number)
print(negativecheck(100))
print(negativecheck(-350))