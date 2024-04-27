if __name__ == '__main__':
    n = int(input().strip())
    for i in range(n):
        print(i**2)


if __name__ == '__main__':
    n = int(input().strip())
    for i in range(1,n+1):
        print(i ,end="")



def is_leap(year):
    leap = False
    
    # Write your logic here
    if year % 4==0:
        leap=True
    if year % 100==0:
        if year % 400 ==0:
            leap =True
        else:
            leap=False
            
                   
    return leap

year = int(input())
print(is_leap(year))
