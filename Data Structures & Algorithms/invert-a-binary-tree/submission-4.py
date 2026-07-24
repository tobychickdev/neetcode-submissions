# Definition for a binary tree node.
# class TreeNode:
#     def __init__(root, val=0, left=None, right=None):
#         root.val = val
#         root.left = left
#         root.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        if not root:
            return None
        
        if root.left and root.right:
            temp = root.right
            root.right = self.invertTree(root.left)
            root.left = self.invertTree(temp)
        elif root.left:
            root.right = self.invertTree(root.left)
            root.left = None
        elif root.right:
            root.left = self.invertTree(root.right)
            root.right = None
        return root    