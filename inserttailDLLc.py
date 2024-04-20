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
    tail=head
    while tail.next!=None:
        tail=tail.next
    curr=tail
    while curr!=None:
        print(curr.data,end="-->")
        curr=curr.prev
    print()

def addNodeAtTailOfLinkedList(head,ele):
    newBlock=Node(ele)
    if head==None:
        return newBlock   
    tail=head
    while tail.next!=None:
        tail=tail.next
    tail.next=newBlock
    newBlock.prev=tail
    return head 
l=[12,23,43,454,23,54]
head=None
for ele in l:
    head=addNodeAtTailOfLinkedList(head,ele)
printleftToRightManner(head)
printrightToLeftManner(head)



