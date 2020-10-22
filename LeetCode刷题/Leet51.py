class Solution:
    def solveNQueens(self, n):
        def could_place(row, col):
            return not (cols[col] + hill_diag[row - col] + dale_diag[row + col])

        def place_queen(row, col):
            queens.add((row, col))
            cols[col], hill_diag[row - col], dale_diag[row + col] = 1, 1, 1

        def remove_queen(row, col):
            queens.remove((row, col))
            cols[col], hill_diag[row - col], dale_diag[row + col] = 0, 0, 0

        def add_solution():
            solution = []
            for r, c in sorted(queens):
                solution.append('.' * c + 'Q' + '.' * (n - c - 1))
            output.append(solution)

        def backtrack(row):
            for col in range(n):
                if could_place(row, col):
                    place_queen(row, col)
                    if row + 1 == n:
                        add_solution()
                    else:
                        backtrack(row + 1)
                    remove_queen(row, col)

        cols = [0] * n
        hill_diag = [0] * (n+n)
        dale_diag = [0] * (n + n)
        queens = set()
        output = []
        backtrack(0)
        return output
a=Solution().solveNQueens(4)
a