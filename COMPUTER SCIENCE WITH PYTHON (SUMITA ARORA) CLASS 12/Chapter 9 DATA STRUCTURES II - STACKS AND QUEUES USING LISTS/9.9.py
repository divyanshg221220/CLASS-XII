#9.9
HighestPr=[]
NormalPr=[]
LowestPr=[]
while True:
    print()
    print("1. Insert Element")
    print("2. Search for Element")
    print("3. Change Priority")
    print("4. EXIT")
    print()
    choice=int(input("USER'S CHOICE:"))
    if choice==1:
        element=input("Enter Element : ")
        priority=input("Priority (Highest/ Normal/ Lowest(H/N/L): ").upper()
        if priority=="H":
            HighestPr.append(element)
        elif priority=="N":
            NormalPr.append(element)
        elif priority=="L":
            LowestPr.append(element)
    elif choice==2:
        element=input("Enter Element : ")
        if element in HighestPr:
            print("HighestPr")
        elif element in NormalPr:
            print("NormalPr")
        elif element in LowestPr:
            print("LowestPr")
        else:
            print("Element not found")
    elif choice==3:
        element=input("Enter Element : ")
        if element in HighestPr:
            q=input("Want to Decrease its priority (Y/N) ? ").upper()
            if q=="Y":
                HighestPr.remove(element)
                NormalPr.append(element)
        elif element in NormalPr:
            q=input("Want to Increase/Decrease its priority (I/D) ? ").upper()
            if q=="I":
                NormalPr.remove(element)
                HighestPr.append(element)
            elif q=="D":
                NormalPr.remove(element)
                LowestPr.append(element)
        elif element in LowestPr:
            q=input("Want to Increase its priority (Y/N) ? ").upper()
            if q=="Y":
                LowestPr.remove(element)
                NormalPr.append(element)
        else:
            print("Element not found")
    elif choice==4:
        print("EXITED BY USER")
        break
    print("HighestPr:",HighestPr)
    print("NormalPr:",NormalPr)
    print("LowestPr:",LowestPr)