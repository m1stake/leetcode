from typing import List


class Solution:

    mvm = {
        'right': [0, 1, 'down'],
        'down': [1, 0, 'left'],
        'left': [0, -1, 'up'],
        'up': [-1, 0, 'right'],
    }

    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:

        if not matrix:
            return []

        r = []
        i = 0

        m = len(matrix)
        n = len(matrix[0]) # 列

        position = [0, -1]
        direction = "right"

        while i < m * n:
            cr = position[0]
            cc = position[1]

            nr, nc = self.mvf(cr, cc, direction)

            if self.should_turn(nr, nc, n, m, matrix):
                direction = Solution.mvm[direction][2]
                nr, nc = self.mvf(cr, cc, direction)

            position[0] = nr
            position[1] = nc

            r.append(matrix[nr][nc])
            matrix[nr][nc] = None

            i += 1

        return r

    def mvf(self, cr, cc, direction):
        mv = Solution.mvm[direction]
        return cr + mv[0], cc + mv[1]

    def should_turn(self, nr, nc, n, m, matrix):
        return nr < 0 or nr == m or nc < 0 or nc == n or (matrix[nr][nc] is None)


print(
    Solution().spiralOrder(
        [
            [1, 2, 3, 4],
            [10, 11, 12, 5],
            [9, 8, 7, 6]
        ]
    ),
)
