class Solution:
    def rob(self, nums: List[int]) -> int:
        # dp[i] = max amount of money you can take up to index i

        dp = nums.copy()
        best_before, prev = 0,0
        
        for i in range(0, len(dp)):
            dp[i] = nums[i] + best_before
            best_before = max(best_before,prev)
            prev = dp[i]
        return max(dp)

        