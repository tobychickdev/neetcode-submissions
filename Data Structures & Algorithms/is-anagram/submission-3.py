class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        charset1 = dict()
        charset2 = dict()

        for c in s:
            if c not in charset1:
                charset1[c] = 1
            else:
                charset1[c] += 1
        
        for c in t:
            if c not in charset2:
                charset2[c] = 1
            else:
                charset2[c] += 1
        
        return charset1 == charset2