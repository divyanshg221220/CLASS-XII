#2.3
fileobject=open("practice.txt","w+")
while True:
    data=input("Enter data to save in the text file: ")
    fileobject.write(data)
    ans=input("Do you wish to enter more data?(y/n): ")
    if ans=='n': break
fileobject.close()