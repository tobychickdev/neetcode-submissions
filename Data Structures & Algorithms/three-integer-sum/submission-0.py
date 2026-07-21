class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        hs = dict()
        resultset = set()
        for x, num in enumerate(nums):
            hs[num] = x
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i == j:
                    continue
                target = 0 - nums[i] - nums[j]
                if target in hs:
                    if hs[target] !=i and hs[target] != j:
                        resultset.add(tuple(sorted([nums[i], nums[j], nums[hs[target]]])))
                j += 1
            i += 1
        return [list(t) for t in resultset]

        