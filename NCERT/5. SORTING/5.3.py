#5.3
def insertion_Sort(list3):
    n=len(list3)
    for i in range(n):
        temp=list3[i]
        j=i-1
        while j>=0 and temp<list3[j] :
            list3[j+1]=list3[j] 
            j=j-1
        list3[j+1]=temp
numList=[8,7,13,1,-9,4]
insertion_Sort(numList)
print("The sorted list is :")
for i in range(len(numList)):
    print(numList[i],end=" ")