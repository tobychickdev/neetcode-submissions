class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        m = {}
        for i, num in enumerate(nums):
            search = target - num
            if search in m:
                return [min(i, m[search]), max(i, m[search])]
            else:
                m[num] = i
        return []

        