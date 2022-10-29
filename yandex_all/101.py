# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root == None:
            return True
        return self.IsOkRec(root.left, root.right)
    
    def IsOkRec(self, left_node, right_node):
        if (left_node == None) & (right_node == None):
            return True
        elif (left_node == None) or (right_node == None):
            return False
        elif left_node.val != right_node.val:
            return False
        return self.IsOkRec(left_node.left, right_node.right) & \
            self.IsOkRec(left_node.right, right_node.left)
