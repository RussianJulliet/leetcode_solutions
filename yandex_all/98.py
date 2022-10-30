# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if (root == None):
            return True
        return self.valid_tree(root, -inf, inf)
        
        
    def valid_tree(self, root, lb, rb):
        if (root == None):
            return True
        else:
            if (root.val <= lb) or (root.val >= rb):
                return False
            return self.valid_tree(root.left, lb, root.val) and self.valid_tree(root.right, root.val, rb)
