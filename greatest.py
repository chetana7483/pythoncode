def numbergreaterthantarget(listofnumbers,target):
   result=0
   n=len(listofnumbers)
   for index in range(n):
      if listofnumber[index]>=target:
          result= result + 1
      return result
listofnumbers=[12,34,21,-12,34,55,56,34,12]     
target=34
result=numbergreaterthantarget(listofnumbers,target)
print("total number greater than target are",result)


