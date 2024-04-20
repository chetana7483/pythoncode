class Node:
    def __init__(self , data):
        self.data=data
        self.next=None
        self.prev=None
def printleftToRightManner(head):
    print("left to right")
    curr=head
    while curr!=None:
        print(curr.data,end="-->")
        curr=curr.next
    print()            

def printrightToLeftManner(tail):
    print("Right to left")
    curr=tail
    while curr!=None:
        print(curr.data,end="-->")
        curr=curr.prev
    print()

obj1 = Node(121)
obj2 = Node(145)
obj3 = Node(678)
obj4 = Node(89)
obj5 = Node(12)
obj1.next=obj2
obj2.prev=obj1
obj2.next=obj3
obj3.prev=obj2
obj3.next=obj4
obj4.prev=obj3
obj4.next=obj5
obj5.prev=obj4
printleftToRightManner(obj1)
printrightToLeftManner(obj5)

