class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = []
        while(len(strs) !=0):
            current = strs[0]
            templist = []
            dict1 = {}

            # make original word dict
            for c in current:
                if c in dict1:
                    dict1[c] += 1
                else:
                    dict1[c] = 1

            #
            dict2 = {}
            for word in strs:
                
                for c in word:
                    if c in dict2:
                        dict2[c] += 1
                    else:
                        dict2[c] = 1
                
                if(dict1 == dict2):
                    templist.append(word)
                dict2 = {}
    
            for w in templist:
                strs.remove(w)
            result.append(templist)
        return result


        
        