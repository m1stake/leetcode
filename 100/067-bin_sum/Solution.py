

class Solution:
    def addBinary(self, a: str, b: str) -> str:

        if (not a) or (not b):
            return a or b

        over = '0'
        r = ''

        if len(a) > len(b):
            b = '0' * (len(a) - len(b)) + b
        else:
            a = '0' * (len(b) - len(a)) + a

        for i in range(len(a) - 1, -1, -1):
            ca = a[i]
            cb = b[i]
            if ca == '1' and cb == '1':
                r = over + r
                over = '1'
            elif ca == '1' or cb == '1':
                if over == '1':
                    r = '0' + r
                else:
                    r = '1' + r
            else:
                r = over + r
                over = '0'

        if over == '1':
            r = '1' + r

        return r


print(
    Solution().addBinary('010', '111110'),
    Solution().addBinary("1010", "1011"),
)
