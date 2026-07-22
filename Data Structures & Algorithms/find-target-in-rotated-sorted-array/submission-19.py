class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1
  
        while l <= r:
            mid = (l+r) // 2
            print(l, mid, r)
            if target == nums[mid]:
                return mid
            if target > nums[mid]:
                if nums[l] <= nums[mid]:
                    l = mid + 1
                elif nums[r] >= target:
                    l = mid + 1
                else:    
                    r = mid - 1
            if target < nums[mid]:
                if nums[l] <= nums[mid]:
                    if nums[l] > target:
                        l = mid + 1
                    else:
                        r = mid - 1
                else:
                    r = mid - 1

        return -1

        
            
            
        