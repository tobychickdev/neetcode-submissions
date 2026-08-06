class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        p = [False] * len(nums)

        def backtrack(perm, pick):
            if len(perm) == len(nums):
                res.append(perm[:])
                return
            for i in range(len(nums)):
                if not pick[i]:
                    perm.append(nums[i])
                    pick[i] = True
                    backtrack(perm, pick)
                    perm.pop()
                    pick[i] = False
        
        backtrack([], p)

        return res
            