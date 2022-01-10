#modules
def duplicate():
    list = [1,2,3,4,5,2,5,"ravi","krish","ravi"]
    uniqueList = []
    dup = []
    for i in list:
        if i not in uniqueList:
            uniqueList.append(i)
        else:
            dup.append(i)
    print(dup)
            
duplicate()
   
    
