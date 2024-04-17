def findgreatestelement(numbers):
   result=0
   n=len(numbers)

   for index in range(n):
      if numbers[index] > result:
         result=numbers[index]
   return result
numbers=[12,3,4,65,43,21,65,1,2,3]
result=findgreatestelement(numbers)
print("greateste element is",result)



def findsmallestelement(numbers):
   result=0
   n=len(numbers)
   for index in range(n):
      if numbers[index] < result:
         result=numbers[index]
   return result
numbers=[12,3,4,65,43,21,65,1,2,3]
result=findsmallestelement(numbers)
print("smallest element is",result)


def findsmallestelement(numbers):
   result=12
   n=len(numbers)
   for index in range(n):
      if numbers[index] < result:
         result=numbers[index]
   return result
numbers=[12,3,4,65,43,21,65,1,2,3]
result=findsmallestelement(numbers)
print("smallest element is",result)
