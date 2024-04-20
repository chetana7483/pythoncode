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
#inserting a value at given specific position       
def insertAtSpecificPosition(head, position, value):
    newBlock = Node(value)
    if position == 1:
        newBlock.next = head 
        return newBlock
 
    index = 1 
    curr = head 
    while index != position - 1:
        curr = curr.next 
        index += 1 
 
    newBlock.next = curr.next
    curr.next = newBlock
    return head

#deleting the head node
def deleteHeadNode(head):
    if head==None:
        return None
    secondNode=head.next
    head.next=None
    return secondNode
#deleting node of a specific position
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
l = [11, 22, 33, 44, 55, 66, 77, 88, 99, 110]
head = None 
for ele in l:
    head = insertNodeAtHeadOfLinkedList(head,ele)
printLinkedList(head)
head = insertAtSpecificPosition(head, 5,6757)
printLinkedList(head)
 
head=deleteHeadNode(head) 
printLinkedList(head)
 
head=deleteNodeAtSpecificPosition(head,3) 
printLinkedList(head)
 
