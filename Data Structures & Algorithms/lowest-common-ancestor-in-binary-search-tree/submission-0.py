# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        ancester = root
        while root:
            if root.val == p.val:
                return root
            if root.val == q.val:
                return root
            if p.val > root.val and q.val > root.val:
                root = root.right
            elif p.val < root.val and q.val < root.val:
                root = root.left            
            elif p.val > root.val and q.val < root.val:
                return root
            elif p.val < root.val and q.val > root.val:
                return root
        return None
        
        
        