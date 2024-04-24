# Trees   
class TreeNode:
    def __init__(self, data):
        self.data = data 
        self.left = None 
        self.right = None 
 
# 1. objects creation (memory allocation) 
root = TreeNode(18)
# root:
# data = 15 
# left = None 
# right = None 
obj2 = TreeNode(15)
obj3 = TreeNode(20)
obj4 = TreeNode(25)
obj5 = TreeNode(30)
obj6 = TreeNode(45)
obj7 = TreeNode(80)
 
#    18 
#   15  20 
# 25 30 45 80
 
 
# 2- establishing links between nodes 
root.left = obj2 
root.right = obj3 
 
obj2.left = obj4 
obj2.right = obj5 
 
obj3.left = obj6 
obj3.right = obj7

 
 
 
 
 
 
 
 
 
 
 


 

 
 
