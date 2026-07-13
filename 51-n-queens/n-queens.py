class Solution:
    def solveNQueens(self, n):
        res = []
        board = [['.' for _ in range(n)] for _ in range(n)]

        cols = set()
        posDiag = set()   # r + c
        negDiag = set()   # r - c

        def backtrack(r):
            if r == n:
                copy = []
                for row in board:
                    copy.append("".join(row))
                res.append(copy)
                return

            for c in range(n):
                if c in cols or (r + c) in posDiag or (r - c) in negDiag:
                    continue

                cols.add(c)
                posDiag.add(r + c)
                negDiag.add(r - c)
                board[r][c] = 'Q'

                backtrack(r + 1)

                board[r][c] = '.'
                cols.remove(c)
                posDiag.remove(r + c)
                negDiag.remove(r - c)

        backtrack(0)
        return res