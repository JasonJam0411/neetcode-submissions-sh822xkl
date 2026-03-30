class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        #row
        for sub in board:
            temp = []
            for i in range(len(sub)):
                if sub[i]=='.':
                    continue

                if sub[i] not in temp:
                    temp.append(sub[i])
                else:
                    return False
        #col
        for i in range(len(board)):
            temp = []
            for j in range(len(board[0])):
                if board[j][i]=='.':
                    continue

                if board[j][i] not in temp:
                    temp.append(board[j][i])
                else:
                    return False

        #3x3
        #0,2  3,5 6,9
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                temp = set() # 這裡建議改用 set，速度更快
                # 遍歷方格內的 9 個格子
                for r in range(i, i + 3):
                    for c in range(j, j + 3):
                        char = board[r][c]
                        if char == '.':
                            continue
                        if char in temp:
                            return False
                        temp.add(char)








        return True