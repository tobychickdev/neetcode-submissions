from collections import deque
class Solution:

    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] != "0":
                    #bfs:
                    print("before dfs:")
                    for row in grid:
                        print(row)
                    def dfs(x, y):
                        print(x,y)
                        grid[x][y] = "0"
                        #right
                        if x < len(grid) and (y+1) < len(grid[i]) and grid[x][y+1] == "1":
                            grid[x][y+1] = "0"
                            dfs(x, y+1)
                        #left
                        if x < len(grid) and (y-1) >= 0 and grid[x][y-1] == "1":
                            grid[x][y-1] = "0"
                            dfs(x, y-1)
                        #down
                        if (x+1) < len(grid) and (y) < len(grid[i]) and grid[x+1][y] == "1":
                            grid[x+1][y] = "0"
                            dfs(x+1, y)
                        if (x-1) >= 0 and (y) < len(grid[i]) and grid[x-1][y] == "1":
                            grid[x-1][y] = "0"
                            dfs(x-1, y)
                    dfs(i, j)
                    islands +=1
                    print("after dfs:")
                    for row in grid:
                        print(row)


        
        return islands

        