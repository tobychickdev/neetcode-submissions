class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        charset1 = dict()
        for ch in s:
            if ch in charset1:
                charset1[ch] += 1
            else:
                charset1[ch] = 1
        charset2 = dict()

        for ch in t:
            if ch in charset2:
                charset2[ch] += 1
            else:
                charset2[ch] = 1
        for ch in s:
            if ch not in charset2:
                return False

            if charset1[ch] != charset2[ch]:
                return False
        for ch in t:
            if ch not in charset1:
                return False

            if charset1[ch] != charset2[ch]:
                return False
        
        return True
        