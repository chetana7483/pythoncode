def totalevennumbers(listofnumbers,target):
   result = 0
   n = len(listofnumbers)
   for index in range(n):
       if listofnumbers[index] % 2 == 0:
            result = result + 1
        return result

listofnumbers = [12,34,21,-12,34,55,56,34,12] 
target = 34    
result = totalevennumbers(listofnumbers,target)
print("total number of even numbers are",result)


