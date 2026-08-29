class Solution:
    def longestPalindrome(self, s: str) -> str:
        maxL = 0
        maxR = 0
        

        for r in range(1, len(s)):
            l = r
            while l >= 0 and r < len(s) and s[l] == s[r] :
                #print(s[l], l, r)
                l -=1
                r += 1
            if r-l-2 > maxR - maxL:
                maxR = r-1
                maxL = l+1
        for l in range(0, len(s)):
            r = l + 1
            while l >= 0 and r < len(s) and s[l] == s[r] :
                #print(s[l], l, r)
                l -=1
                r += 1
            if (r-l-2) > maxR - maxL:
                maxR = r-1
                maxL = l+1
        
        return s[maxL:maxR+1]
        



        
        