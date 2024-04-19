try:
    a=10/0
except:
    print("some exception raises")
else:
    print("no exception raised,everthing worked properly")
print("outside the try block")            


print("starting line")
a=[11,22,33,44]
print(a)

try:
    a=10/0
    print(a[5])
except:
    print("some exception raises")
else:
    print("no exception raised,everthing worked properly")
finally:
    print("this is a finally block")    
print("outside the try block")            




print("starting line")
a=[11,22,33,44]
try:
    #a=10/0
    #print(a[4])
    print(z)
except ZeroDivisionError:
    print("exception raised due to zero division error")
except IndexError:
    print("exception raised due to index out of range")   
except NameError:
    print("exception  raised due to undefined variable ")
except:
    print("some exception raises")     
else:
    print("no exception raised,everthing worked properly")
finally:
    print("this is a finally block")    
print("outside the try block")  



