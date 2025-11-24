#8.2
def unique(lst):
    if lst!=[]:
        list=[]
        for i in lst:
            if i not in list:
                list.append(i)
        print(list)
    else:
        print("Empty list")
lst=eval(input("Enter a list: "))
unique(lst)