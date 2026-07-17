class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleanstr = ""
        for c in s:
            if c.isalnum():
                cleanstr += c.lower()
        return cleanstr == cleanstr[::-1]

        