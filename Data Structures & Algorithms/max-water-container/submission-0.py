class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_volume = 0
        for i, h1 in enumerate(heights):
            for j, h2 in enumerate(heights):
                if i == j:
                    continue
                step = abs(i-j)
                volume = min(h1, h2) * step
                if volume > max_volume:
                    max_volume = volume

        return max_volume