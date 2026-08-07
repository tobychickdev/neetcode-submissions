class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def dfs(o, c, cur):
            if c > o:
                return
            if len(cur) == 2*n:
                if o == c:
                    res.append(cur[:])
                return
            cur += "("
            dfs(o+1, c, cur)
            cur = cur[:-1]
            cur += ")"
            dfs(o, c+1, cur)
        dfs(0, 0, "")

        return res

            
            

        