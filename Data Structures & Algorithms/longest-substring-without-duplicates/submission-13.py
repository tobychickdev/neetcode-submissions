class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s == "":
            return 0
        
        max_sub = 0
        l,r = 0,0
        cs = set()
        while r < len(s):
            if s[r] not in cs:
                cs.add(s[r])
                r += 1
            else:
                max_sub = max(max_sub, r-l)
                cs.remove(s[l])
                l += 1
        max_sub = max(max_sub, r-l)
        return max_sub

            

                
            
        