g=[12,34,21,-12,34,55,56]
n=len(g)
target=34
result=0
for index in range(n):
    if g[index]==target:
        result=result+1
print("total number of occurances are",result)


def findtataloccurence(listofnumbers,target):
result=0
n=len(listofnumbers)
for index in range(n):
    if listofnumbers[index]==target:
        result=result+1
        return result
listofnumbers=[12,34,21,-1234,55,56,34,12]     
target=35
result=findtotaloccurences(listofnumbers,target)
print("total number of occurances are",result)

list2=[12,23,54,56,4,3,2,1,23,45,23]
target2=23
result2=findtotaloccurence(list2,target2)
print(result2)


