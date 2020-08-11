from typing import List


class Solution:

    mvm = {
        'right': [0, 1, 'down'],
        'down': [1, 0, 'left'],
        'left': [0, -1, 'up'],
        'up': [-1, 0, 'right'],
    }

    def generateMatrix(self, n: int) -> List[List[int]]:

        m = [[0] * n for _ in range(n)]

        position = [0, -1]
        direction = "right"
        i = 0

        while i < n * n:

            cr = position[0]
            cc = position[1]

            nr, nc = self.mvf(cr, cc, direction)

            if self.should_turn(nr, nc, n, m):
                direction = Solution.mvm[direction][2]
                nr, nc = self.mvf(cr, cc, direction)

            position[0] = nr
            position[1] = nc

            m[nr][nc] = i + 1

            i += 1
        return m

    def mvf(self, cr, cc, direction):
        mv = Solution.mvm[direction]
        return cr + mv[0], cc + mv[1]

    def should_turn(self, nr, nc, n, m):
        return nr < 0 or nr == n or nc < 0 or nc == n or (not m[nr][nc] == 0)


print(
    Solution().generateMatrix(4),
)
