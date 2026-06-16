#2.5
fileobject=open("report.txt","w+")
print("WRITING DATA IN THE FILE")
print()
while True:
    line=input("Enter a sentence ")
    fileobject.write(line)
    fileobject.write('\n')
    choice=input("Do you wish to enter more data? (y/n): ")
    if choice in ('n','N'): break
print("The byte position of file object is ",fileobject.tell())
fileobject.seek(0)
print()
print("READING DATA FROM THE FILE")
str=fileobject.read()
print(str)
fileobject.close()