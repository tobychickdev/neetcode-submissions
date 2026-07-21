class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s == "":
            return 0
        charset = set()
        maxC = 1
        l = 0
        r = 1
        charset.add(s[l])

        while r < len(s):
            if s[r] in charset:
                maxC = max(maxC, r - l)
                l += 1
                charset.clear()
                charset.add(s[l])
                r = l + 1
            else:
                charset.add(s[r])
                r += 1
        maxC = max(maxC, r-l)
        return maxC
            

                
            
        