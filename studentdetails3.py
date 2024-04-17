lass box:
    def __init__(self,currname,currrollnum,currdbmsmarks,currosmarks,currdsmarks,currjavamarks,currcmarks):
        self.name=currname
        self.rollnumber=currrollnum
        self.dbmsmarks=currdbmsmarks
        self.osmarks=currosmarks
        self.dsmarks=currdsmarks
        self.javamarks=currjavamarks
        self.cmarks=currcmarks

student1=box("raju",1,98,96,95,95,90)
print(student1.name)
print(student1.rollnumber)
print(student1.dbmsmarks)
print(student1.cmarks)

student2=box("seetha",2,96,93,92,89,84)
print(student2.name)
print(student2.rollnumber)
print(student2.dbmsmarks)
print(student2.cmarks)


