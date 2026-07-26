import heapq as h
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-i for i in stones]
        h.heapify(stones)
        
        while len(stones) > 1:
            y = h.heappop(stones)
            x = h.heappop(stones)

            if x !=y:
                h.heappush(stones, y-x)
        if len(stones) == 1:
            return -stones[0]
        return 0

        
        