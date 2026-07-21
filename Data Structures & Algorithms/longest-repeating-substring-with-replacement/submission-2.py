class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # Find the longest repeated substring allowing k - skips
        # Sliding Window
        if s == "":
            return 0
        l = 0
        r = 0
        window_freq = [0] * 26
        longest_sub = 0

        while r < len(s):
            window_freq[ord(s[r]) - ord('A')] += 1
            cond = (r-l + 1) - max(window_freq)
            if cond <= k:
                longest_sub = max(longest_sub, r-l+1)
            else:
                window_freq[ord(s[l]) - ord('A')] -= 1
                l += 1
            r += 1


        return longest_sub
