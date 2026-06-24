class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        for r in range(9):
            for c in range(9):
                if board[r][c] != ".":
                    n = board[r][c]
                    rows[r].add(n)
                    cols[c].add(n)
                    boxes[(r//3)*3 + c//3].add(n)

        def backtrack(r, c):

            if r == 9:
                return True

            if c == 9:
                return backtrack(r+1, 0)

            if board[r][c] != ".":
                return backtrack(r, c+1)

            for n in "123456789":

                b = (r//3)*3 + c//3

                if n not in rows[r] and n not in cols[c] and n not in boxes[b]:

                    board[r][c] = n
                    rows[r].add(n)
                    cols[c].add(n)
                    boxes[b].add(n)

                    if backtrack(r, c+1):
                        return True

                    board[r][c] = "."
                    rows[r].remove(n)
                    cols[c].remove(n)
                    boxes[b].remove(n)

            return False

        backtrack(0, 0)