class Node:
    def __init__(self, data):
        self.data = data 
        self.next = None
 
def printLinkedList(head):
    curr = head
    while curr != None:
        print(curr.data, end = " --> ")
        curr = curr.next
    print()
def insertNodeAtHeadOfLinkedList(head,ele):
    newBlock=Node(ele)
    if head==None:
      return newBlock
    newBlock.next=head
    return newBlock  
#deleting the head node
def deleteHeadNode(head):
    if head==None:
        return None
    secondNode=head.next
    head.next=None
    return secondNode

#deleting node at specific position
def deleteNodeAtSpecificPosition(head,position):
    if position==1:
        return deleteHeadNode(head)
    curr= head
    index=1
    while index!=position-1:
        curr=curr.next
        index+=1
    mainNode=curr.next
    nextNode=mainNode.next
    mainNode.next=Node
    curr.next=None
    curr.next=nextNode
    return head    
n=int(input())
l=list(map(int,input().split()))
head = None 
for ele in l:
    head = insertNodeAtHeadOfLinkedList(head,ele)
printLinkedList(head)

head=deleteHeadNode(head) 
printLinkedList(head)
 
head=deleteNodeAtSpecificPosition(head,3) 
printLinkedList(head)
 
