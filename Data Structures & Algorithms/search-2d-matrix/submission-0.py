class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        new = []
        for row in matrix:
            for item in row:
                new.append(item)

        def bin_search(nums):
            if nums == []:
                return False
            mid = len(nums) // 2
            if nums[mid] == target:
                return True
            if nums[mid] > target:
                return bin_search(nums[:mid])
            if nums[mid] < target:
                return bin_search(nums[mid+1:])
        return bin_search(new)


        