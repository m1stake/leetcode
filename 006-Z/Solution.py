
class Solution:

    def convert(self, s: str, numRows: int) -> str:
        """
        1     7       13
        2   6 8    12 14
        3 5   9 11    15
        4     10      16
        """

        if numRows == 1:
            return s

        result = ''
        # 逐行，
        for rn in range(numRows):
            i_cur = rn
            cn = 0
            # 判断是否超出长度
            while i_cur < len(s):
                # 判断是否有数
                if self.has_num(numRows, rn, cn):
                    result = result + s[i_cur]

                cn = cn + 1
                # 每列加2
                i_cur = i_cur + 2

        return result

    def has_num(self, numRows, rn, cn):
        return (cn % (numRows - 1) == 0) or (cn % (numRows - 1) == (numRows - 1 - rn))
