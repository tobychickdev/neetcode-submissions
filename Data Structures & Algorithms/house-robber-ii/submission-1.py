class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        dp0 = nums[:-1]
        print(dp0)
        dp1 = nums[1:]
        print(dp1)
        bestbefore, prev = 0, 0
        for i in range(0,len(dp0)):
            dp0[i] = nums[i] + bestbefore
            bestbefore = max(bestbefore, prev)
            prev = dp0[i]
        bestbefore, prev = 0, 0
        for i in range(0,len(dp1)):
            print(dp1)
            print(bestbefore)
            dp1[i] = nums[i+1] + bestbefore
            bestbefore = max(bestbefore, prev)
            prev = dp1[i]
        print(dp1)

        return max(max(dp1), max(dp0))
        