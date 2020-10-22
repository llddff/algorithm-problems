class Solution:
    def solveSudoku(self, board):
        def flip(i, j, digit):
            line[i] ^= (1 << digit)
            col[j] ^= (1 << digit)
            block[i // 3][j // 3] ^= (1 << digit)

        def dfs(pos):
            nonlocal valid
            if pos == len(spaces):
                valid = True
                return
            i, j = spaces[pos]
            mask = ~(line[i] | col[j] | block[i // 3][j // 3]) & 0x1ff
            while mask:
                digmask = mask & (-mask)
                digit = bin(digmask).count('0') - 1
                flip(i, j, digit)
                board[i][j] = str(digit + 1)
                dfs(pos + 1)
                flip(i, j, digit)
                mask &= (mask - 1)
                if valid:
                    return

        line = [0] * 9
        col = [0] * 9
        block = [[0] * 3 for i in range(3)]
        valid = False
        spaces = []
        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    digit = int(board[i][j]) - 1
                    flip(i, j, digit)
        while True:
            moved = False
            for i in range(9):
                for j in range(9):
                    if board[i][j] == '.':
                        mask = ~(line[i] | col[j] | block[i // 3][j // 3]) & 0x1ff
                        if not (mask & (mask - 1)):
                            digit = bin(mask).count('0') - 1
                            flip(i, j, digit)
                            board[i][j] = str(digit + 1)
                            moved = True
            if not moved:
                break
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    spaces.append((i, j))
        dfs(0)
