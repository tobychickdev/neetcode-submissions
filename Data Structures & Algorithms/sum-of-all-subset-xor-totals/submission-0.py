class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        total = 0
        result = []

        def dfs(start, current):
            nonlocal total
            result.append(current[:])
            if current:
                acc = current[0]
                for i in range(1, len(current)):
                    acc = acc ^ current[i]
                total += acc

            for i in range(start, len(nums)):
                current.append(nums[i])
                dfs(i+1, current)
                current.pop()

        dfs(0, [])
               

        return total


            
        
        