class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        if not matrix:
            return False


        def bin_search(nums):
            if nums == []:
                return False
            mid = len(nums) // 2
            print("search",nums, nums[mid])

            if nums[mid] == target:
                print("found", nums[mid])
                return True
            if nums[mid] > target:
                return bin_search(nums[:mid])
            if nums[mid] < target:
                return bin_search(nums[mid+1:])

        mid = len(matrix) // 2
        start = matrix[mid][0]
        end = matrix[mid][-1]
        print(matrix[mid], start, end)
        if target >= start and target <= end:
            return bin_search(matrix[mid])
        elif len(matrix) == 1:
            return False
        elif target < start:
            return self.searchMatrix(matrix[:mid], target)
        elif target > end:
            return self.searchMatrix(matrix[mid+1:], target)

        