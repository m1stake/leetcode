from typing import List


class Solution:

    def isValidSudoku(self, board: List[List[str]]) -> bool:

        imap = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8]
        ]

        # 行
        for i in range(9):
            row = 0
            for j in range(9):
                c = board[i][j]
                if c == '.':
                    continue
                ci = int(c)
                if (1 << ci & row) > 0:
                    return False
                else:
                    row += 1 << ci

        # 列
        for i in range(9):
            column = 0
            for j in range(9):
                c = board[j][i]
                if c == '.':
                    continue
                ci = int(c)
                if (1 << ci & column) > 0:
                    return False
                else:
                    column += 1 << ci

        # 块
        for bi in imap:
            for bj in imap:
                block = 0
                for i in bi:
                    for j in bj:
                        c = board[i][j]
                        if c == '.':
                            continue
                        ci = int(c)
                        if (1 << ci & block) > 0:
                            return False
                        else:
                            block += 1 << ci

        return True


print(
    Solution().isValidSudoku(
        [
            ["5","3",".",".","7",".",".",".","."],
            ["6",".",".","1","9","5",".",".","."],
            [".","9","8",".",".",".",".","6","."],
            ["8",".",".",".","6",".",".",".","3"],
            ["4",".",".","8",".","3",".",".","1"],
            ["7",".",".",".","2",".",".",".","6"],
            [".","6",".",".",".",".","2","8","."],
            [".",".",".","4","1","9",".",".","5"],
            [".",".",".",".","8",".",".","7","9"]
        ]
    ),
    Solution().isValidSudoku(
        [
            ["8","3",".",".","7",".",".",".","."],
            ["6",".",".","1","9","5",".",".","."],
            [".","9","8",".",".",".",".","6","."],
            ["8",".",".",".","6",".",".",".","3"],
            ["4",".",".","8",".","3",".",".","1"],
            ["7",".",".",".","2",".",".",".","6"],
            [".","6",".",".",".",".","2","8","."],
            [".",".",".","4","1","9",".",".","5"],
            [".",".",".",".","8",".",".","7","9"]
        ]
    )
)