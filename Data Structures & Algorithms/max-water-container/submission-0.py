class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1
        max_volume = 0
        while l < r:
            volume = min(heights[l], heights[r]) * abs(l-r)
            max_volume = max(max_volume, volume)
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        return max_volume

        