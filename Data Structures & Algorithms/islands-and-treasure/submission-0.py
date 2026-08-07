from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        queue = deque()

        for m in range(len(grid)):
            for n in range(len(grid[0])):
                if grid[m][n] == 0:
                    queue.append((m,n))

        
        while queue:
            r, c = queue.popleft()
            for dr,dc in [(1, 0),(0, 1),(-1, 0),(0, -1)]:
                nr, nc = r + dr, c+dc

                if min(nr, nc) >= 0 and nr < len(grid) and nc < len(grid[0]):
                    if grid[nr][nc] == 2147483647:
                        grid[nr][nc] = grid[r][c] + 1
                        queue.append((nr,nc))
                    

        