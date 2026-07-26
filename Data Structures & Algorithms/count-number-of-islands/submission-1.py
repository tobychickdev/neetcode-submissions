from collections import deque
class Solution:

    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] != "0":
                    #dfs:
                    def dfs(x, y):
                        if x < 0 or y < 0 or x >= len(grid) or y >= len(grid[i]) or grid[x][y] == "0":
                            return
                        grid[x][y] = "0"
                        dfs(x+1,y)
                        dfs(x,y+1)
                        dfs(x-1,y)
                        dfs(x,y-1)
                    dfs(i, j)
                    islands +=1
        return islands


        