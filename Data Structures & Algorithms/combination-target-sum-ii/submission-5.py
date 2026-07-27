class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        sublist = []
        candidates.sort()
        def dfs(i):
            if sum(sublist) == target:
                res.append(sublist.copy())
                return
            if i == len(candidates) or sum(sublist) > target:
                return
            sublist.append(candidates[i])
            dfs(i + 1)
            sublist.pop()
            while i + 1 < len(candidates) and candidates[i] == candidates[i+1]:
                i+=1
            dfs(i+1)
        dfs(0)
        return res