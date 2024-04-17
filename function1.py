def solveIt2():
    print("this is line 123")
def solveIt4():
    print("iam solveit4")
    print("this is getting executed")
    solveIt2()
def solveIt():
    print("this is line 111")
    print("this is line 112")
    solveIt4()
def sumoftwonumbers(num1,num2):
    solveIt()
    result=num1+num2
    return result
num1=int(input())
num2=int(input())
result=sumoftwonumbers(num1,num2)
print(result)
