class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        freq_s1 = dict()
        freq_s2 = dict()

        if len(s1) > len(s2):
            return False
        # make freq for s2 to compare on
        for c in s1:
            freq_s1[c] = freq_s1.get(c, 0) + 1

        for i in range(len(s1)):
            print(i)
            print(len(s2))
            freq_s2[s2[i]] = freq_s2.get(s2[i], 0) + 1

        for r in range(len(s1), len(s2)):
            l = r - len(s1)
            if freq_s1 == freq_s2:
                return True
            freq_s2[s2[l]] -= 1
            if freq_s2[s2[l]] == 0:
                del freq_s2[s2[l]]
            freq_s2[s2[r]] = freq_s2.get(s2[r], 0) + 1

        return freq_s1 == freq_s2

        

        
        