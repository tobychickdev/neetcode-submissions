class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sfreq = dict()
        tfreq = dict()
        for ch in s:
            if ch in sfreq:
                sfreq[ch] += 1
            else:
                sfreq[ch] = 1
        for ch in t:
            if ch in tfreq:
                tfreq[ch] += 1
            else:
                tfreq[ch] = 1
        
        return sfreq == tfreq
            

        

        