class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = dict()
        for i in range(len(nums)):
            difference = target - nums[i]
            if difference in hashmap:
                return [min(i, hashmap[difference]), max(i, hashmap[difference])]
            else:
                hashmap[nums[i]] = i
        return true
            


        