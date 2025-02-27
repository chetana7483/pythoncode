import numpy as np
x=np.array([1,2,3,4,5])
print(x)

import numpy as np
x=np.zeros((3,4))
print(x)

import numpy as np
x=np.ones((3,4))
print(x)

import numpy as np
x=np.empty(4)
print(x)

import numpy as np
x=np.eye(4)
print(x)
#it print diagonal elemens

import numpy as np
x=np.add(3,4)
print(x)

import numpy as np
x=np.array([1,2,3])
print(np.cumsum(x))

import numpy as np
lists = np.array([[1, 2, 4], [4, 5, 6], [6, 7, 8]])
for lst in lists:
    print(lst)
x=np.subtract(3,4)
print(x)

import numpy as np
lists = np.array([[1, 2, 4], [4, 5, 6], [6, 7, 8]])
for lst in lists:
    print(lst)

arr1=[1,2,3,4,5,6]
arr2=[[1,2,3],[4,5,6]]
for i in range(len(arr2)):
    for j in range(len(arr2[i])):
        if i==j or i+j==2:
            arr2[i][j]=0
        print(arr2[i][j],end=" ")
    print()   
  

arr= [[1, 2, 3],[4, 5, 6],[7, 8, 9]]

transposed = [[arr[j][i] for j in range(len(arr))] for i in range(len(arr[0]))]
for row in transposed:
    print(row)

import numpy as np
var3=np.array([1,2,3,4,5,6,7,8,9,10,11,12,])
print(var3)
x1=var3.reshape(2,3,2)
print(x1)
var=x1.reshape(-1)
print(var)


import numpy as np
var1=np.array([[[1,2,3,4],[1,2,3,4]]])
for k in var1:
    for n in k:
        for m in n:
            print(m) 

import numpy as np
var1=np.array([[[1,2,3,4],[1,2,3,4]]])
for k in np.nditer(var1):
    print(k)
