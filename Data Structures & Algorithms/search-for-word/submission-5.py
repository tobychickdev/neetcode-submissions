class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        path = set()
        def dfs(x, y, cur, visited):
            if x < 0 or x >= len(board) or y <0 or y >= len(board[0]):
                return
            if (x,y) in path:
                return
            cur += board[x][y]
            visited.add((x,y))
            if cur == word:
                print("found Cat")
                return True
            if cur != word[:len(cur)]:
                return
            
            #explore up
            path.add((x,y))
            if dfs(x-1, y, cur[:], visited): return True
            #explore down
            if dfs(x+1, y, cur[:], visited): return True
            #eplore left
            if dfs(x, y-1, cur[:], visited): return True
            if dfs(x, y+1, cur[:], visited): return True
            path.remove((x,y))
            
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == word[0]:
                    if dfs(i, j, "", set()):
                        return True
        
        return False
        