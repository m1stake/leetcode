from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:

        if numRows == 0:
            return []

        if numRows == 1:
            return [[1]]

        r = [[1]]
        pre_row = [1]

        for i in range(1, numRows):
            row = [1]
            for j in range(1, i):
                row.append(pre_row[j-1] + pre_row[j])
            row.append(1)
            r.append(row)
            pre_row = row

        return r


print(
    Solution().generate(0),
    Solution().generate(1),
    Solution().generate(2),
    Solution().generate(3),
    Solution().generate(4),
)
