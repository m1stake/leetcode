
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

        result = []
        step = 2 * (numRows - 1)
        # 逐行，
        for rn in range(numRows):
            loop = 0

            while True:
                i_cur = loop * step + rn
                if i_cur < len(s):
                    result.append(s[i_cur])
                else:
                    break

                # 不是第一行和最后一行
                if not (rn == 0 or rn == (numRows - 1)):
                    i_cur = i_cur + (numRows - 1 - rn) * 2
                    if i_cur < len(s):
                        result.append(s[i_cur])
                    else:
                        break

                loop = loop + 1

        return ''.join(result)

