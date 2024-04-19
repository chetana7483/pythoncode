actualpassword = 4567
attemptscount=3
for i in range(3):
    currentpassword = int(input())
    if currentpassword == actualpassword:
        print("successfully logged in")
        break
    else:
        if attemptscount==1:
            print("you account is blocked try after 24 hours")
        else:
            print("incorrect password you left with ",attemptscount-1,"attempts") 
    attemptscount-=1 
print("starting line")

