class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        # check name is the same, check that there is a common email
        # brute force: for each row, create a set of the emails, check every other row and if names match, check that at least one email is in the set then add these emails to set
        names = dict() 
        for account in accounts:            
            temp = set()
            for i in range(1, len(account)):
                temp.add(account[i])
            if account[0] in names:
                found = False
                for s in names[account[0]]:
                    if not temp.isdisjoint(s):
                        s.update(temp)
                        found = True
                        break
                if not found:
                    names[account[0]].append(temp)
            else:
                names[account[0]] = [temp]        
        result = []

        for k, v in names.items():
            for i in range(len(v)):
                for j in range(len(v)):
                    if i == j: continue
                    if not v[i].isdisjoint(v[j]):
                        v[i].update(v[j])
                        v[j].clear()
        for k, v in names.items():
            for emailSet in v:
                if emailSet:

                    result.append([k] + sorted(list(emailSet)))
        return result
                
