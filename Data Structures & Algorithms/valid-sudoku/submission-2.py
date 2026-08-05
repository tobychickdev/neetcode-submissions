from collections import Counter
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        valid = {1: 1, 2: 1, 3: 1, 4: 1, 5: 1, 6: 1, 7: 1, 8: 1, 9: 1}
        # row check
        for row in board:
            hs = set()
            for num in row:
                if num == ".":
                    continue
                if num in hs:
                    print(num, "in hs")
                    return False
                else:
                    hs.add(num)
        
        for i in range(9):
            hs = set()
            for row in board:
                if row[i] == ".":
                    continue
                if row[i] in hs:
                    print(row[i], "in hs")
                    return False
                else:
                    hs.add(row[i])

        hs = set()
        for i,row in enumerate(board):
            if i % 3 == 0:
                hs.clear()
            for x in range(3):
                if row[x] == ".":
                    continue
                if row[x] in hs:
                    print(row[x], "in hs")
                    return False
                else:
                    hs.add(row[x])
        for i,row in enumerate(board):
            if i % 3 == 0:
                hs.clear()
            for x in range(3,6):
                if row[x] == ".":
                    continue
                if row[x] in hs:
                    print(row[x], "in hs")
                    return False
                else:
                    hs.add(row[x])

                
        for i,row in enumerate(board):
            if i % 3 == 0:
                hs.clear()
            for x in range(6,9):
                if row[x] == ".":
                    continue
                if row[x] in hs:
                    print(row[x], "in hs")
                    return False
                else:
                    hs.add(row[x])
        return True





        return True
                

            
        

        
        