import heapq as h
from collections import deque

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = [0] * 26
        for letter in tasks:
            freq[ord(letter) - ord("A")] -= 1
    
        freq.sort()
        heap = []
        for num in freq:
            if num ==0:
                break
            h.heappush(heap, num)

        q = deque()
        time = 0
        while heap or q:
            if q and q[0][1] == time:
                h.heappush(heap, q.popleft()[0])
                continue
            if not heap:
                time = q[0][1]
                continue
            num = h.heappop(heap) + 1
            if num != 0:
                q.append((num, time + n + 1))
            time += 1
        return time



        