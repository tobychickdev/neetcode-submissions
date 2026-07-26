class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        maxArea = 0

        for i in range(ROWS):
            for j in range(COLS):
                print(i, j, grid[i][j])
                if grid[i][j] == 1:
                    area = 0
                    print(i, j)
                    def dfs(x,y):
                        nonlocal area
                        if x < 0 or y < 0 or x >= ROWS or y >= COLS or grid[x][y] == 0:
                            return
                        grid[x][y] = 0
                        area += 1
                        dfs(x+1, y)
                        dfs(x-1, y)
                        dfs(x, y+1)
                        dfs(x, y-1)
                    print("bfeore dfs")
                    for row in grid:
                        print(row)
                    
                    dfs(i,j)
                    print("after dfs")
                    for row in grid:
                        print(row)
                    print(area)
                    maxArea = max(maxArea, area)
                    area = 0
        return maxArea
        