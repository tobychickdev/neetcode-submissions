class Solution:
    def rob(self, nums: List[int]) -> int:
        # dp[i] = max amount of money you can take up to index i
        if len(nums) == 1:
            return nums[0]
        dp = nums.copy()
        best_before = nums[0]
        prev = nums[1]
        
        for i in range(2, len(dp)):
            dp[i] = nums[i] + best_before
            best_before = max(best_before,prev)
            prev = dp[i]
        print(dp)
        return max(dp)

        