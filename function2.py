print("hello function")

def solveIt2():
    print("this is first line getting excetued")
    print("this is line 123")

print("iam not getting printed")
def solveIt4():
    print("iam solveit4")
    print("this is getting executed")
    solveIt2()
    print("second line is getting exwecuted")

def solveIt():
    print("this is line 111")
    print("this is line 112")
    solveIt4()
    print("solveIt4 haven't compeleted it's exceution ")

def sumoftwonumbers(num1,num2):
    print("after execution")
    solveIt()
    print("nothing gets printed")
    result=num1+num2
    print("before execution")
    return result
    
print("last line is getting printed")    
num1=int(input())
num2=int(input())
result=sumoftwonumbers(num1,num2)
print(result)
print("first line is getting executed")



