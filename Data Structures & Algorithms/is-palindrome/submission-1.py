class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleanstr = ""
        for c in s:
            if c.isalnum():
                cleanstr += c.lower()
        i = 0
        while i < len(cleanstr) - 1 - i:
            if cleanstr[i] != cleanstr[len(cleanstr) - 1 - i]:
                return False
            i += 1
        return True
        