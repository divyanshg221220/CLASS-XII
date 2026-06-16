#2.4
fileobject=open("practice.txt","r")
str=fileobject.readline()
while str:    
    print(str)
    str=fileobject.readline()
fileobject.close()