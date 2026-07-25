# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        maxDepth = self.getDepth(root)
        print(maxDepth)
        depth = 0
        result = []
        for i in range(maxDepth):
            result.append([])
        queue = []
        queue.append(root)
        while depth < maxDepth:
            for i in range(2**depth):
                node = queue[0]
                queue = queue[1:]
                if node:
                    queue.append(node.left)
                    queue.append(node.right)
                    result[depth].append(node.val)
                else:
                    queue.append(None)
                    queue.append(None)
            depth += 1
        return result


        
    def getDepth(self, root):
        if not root:
            return 0
        else:
            return 1 + max(self.getDepth(root.left), self.getDepth(root.right))


        




        