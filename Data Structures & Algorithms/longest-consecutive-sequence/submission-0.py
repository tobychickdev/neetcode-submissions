class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if nums == []:
            return 0
        #if len(nums) == 1:
            #return 1
        
        nums.sort()

        current_seq = 1
        maxcon = 0
        print(nums)

        for r in range(1, len(nums)):
            
            if nums[r] == nums[r-1]:
                continue
            if nums[r] == nums[r-1] + 1:
                current_seq += 1
            else:
                maxcon = max(maxcon, current_seq)
                current_seq = 1
        
        maxcon = max(maxcon, current_seq)
        return maxcon
            