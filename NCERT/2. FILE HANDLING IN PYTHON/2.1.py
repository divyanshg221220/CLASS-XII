#2.1
fobject=open("testfile.txt","w")   
sentence=input("Enter the contents to be written in the file: ")
fobject.write(sentence)    
fobject.close()            
print("Now reading the contents of the file: ")
fobject=open("testfile.txt","r")
for str in fobject:   
    print(str)
fobject.close()