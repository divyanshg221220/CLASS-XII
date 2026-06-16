#5.1
def bubble_Sort(list1):
    n=len(list1)
    for i in range(n):
        for j in range(0,n-i-1):
            if list1[j]>list1[j+1] :    
                list1[j],list1[j+1]=list1[j+1],list1[j]
numList=[8,7,13,1,-9,4]
bubble_Sort(numList)
print("The sorted list is :")
for i in range(len(numList)):
    print(numList[i],end=" ")