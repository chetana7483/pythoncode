#dynamically constructing linked list
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        
def insertAtEndofTail(head,ele):
    newBlock=Node(ele)
    if head==None:
        return newBlock
    curr=head
    while curr.next!= None:
        curr=curr.next
    curr.next=newBlock
    return head
def printLinkedList(head):
    curr=head
    while curr!=None:
        print(curr.data,end=" ")
        curr=curr.next
    print()    

n=int(input())
l=list(map(int,input().split()))
head=None
for ele in l:
    head=insertAtEndofTail(head,ele)
printLinkedList(head)    
    
