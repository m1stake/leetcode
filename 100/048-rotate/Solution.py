from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.

        (0, +3), (+1, +2), (+2, +1), (+3 0)
                                   ,
                                   ,
        (-3, 0),                   , (0, -3)
        """

        if not matrix:
            return

        # 分层，外层到内层
        for layer_no in range(len(matrix) // 2):

            _x = _y = layer_no
            layer_len = len(matrix) - layer_no * 2

            # 逐个圈交换
            for circle_no in range(len(matrix) - layer_no * 2 - 1):

                x0 = _x
                y0 = _y + circle_no

                # 0 -> 1
                x1 = x0 + circle_no
                y1 = y0 + layer_len - 1 - circle_no
                t = matrix[x1][y1]
                matrix[x1][y1] = matrix[x0][y0]
                matrix[x0][y0] = t

                # 1 -> 2
                x2 = x1 + layer_len - 1 - circle_no
                y2 = y1 - circle_no
                t = matrix[x2][y2]
                matrix[x2][y2] = matrix[x0][y0]
                matrix[x0][y0] = t

                # 2-> 3, 3 -> 0
                x3 = x2 - circle_no
                y3 = y2 - layer_len - 1 + circle_no
                t = matrix[x3][y3]
                matrix[x3][y3] = matrix[x0][y0]
                matrix[x0][y0] = t

        for row in matrix:
            print(row)
        print("")


Solution().rotate([]),
Solution().rotate([
    [1,2,3],
    [4,5,6],
    [7,8,9]
]),
Solution().rotate([
    [ 5, 1, 9,11],
    [ 2, 4, 8,10],
    [13, 3, 6, 7],
    [15,14,12,16]
]),
Solution().rotate([
    [1,2,3,4,5],
    [6,7,8,9,10],
    [11,12,13,14,15],
    [16,17,18,19,20],
    [21,22,23,24,25]
]),












