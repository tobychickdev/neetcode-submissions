# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        if not root:
            return 0   

        target = k-1
        nodes_smaller = self.countTree(root.left)
        print("Target:", target, "nodes smaller:", nodes_smaller)
        if nodes_smaller == target:
            return root.val
        if nodes_smaller > target:
            return self.kthSmallest(root.left, k)
        else:
            return self.kthSmallest(root.right, k-nodes_smaller-1)
    def countTree(self, root):
        if not root:
            return 0
        else:
            return 1 + self.countTree(root.left) + self.countTree(root.right)
