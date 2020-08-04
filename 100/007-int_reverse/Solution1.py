

class Solution:

    MAX_INT = 2147483647
    MIN_INT = -2147483648
    MAX_INT_S = '2147483647'
    MIN_INT_S = '2147483648'
    OVERFLOW_LEN = 10
    SIZE_TABLE = [9, 99, 999, 9999, 99999, 999999, 9999999, 99999999, 999999999, MAX_INT]

    def reverse(self, x: int) -> int:
        if x < 0:
            flag = 0
            if x == Solution.MIN_INT:
                return 0
            else:
                x = -x
        else:
            flag = 1

        int_len = self.int_len(x)

        if int_len == Solution.OVERFLOW_LEN:
            return self.reverse_with_check(flag, x)
        else:
            return self.reverse0(flag, x, int_len)

    def int_len(self, x):
        for i in range(Solution.OVERFLOW_LEN):
            if x <= Solution.SIZE_TABLE[i]:
                return i + 1
        raise Exception("int size overflow")

    def reverse0(self, flag, x, int_len):
        r = 0
        for i in range(int_len):
            ip = (x % (10 ** (i + 1))) // (10 ** i)
            r += ip * (10 ** (int_len - 1 - i))
        if flag == 1:
            return r
        else:
            return -r

    def reverse_with_check(self, flag, x):
        int_len = Solution.OVERFLOW_LEN
        if flag == 1:
            ms = Solution.MAX_INT_S
        else:
            ms = Solution.MIN_INT_S

        need_check = True
        r = 0
        for i in range(int_len):
            ip = (x % (10 ** (i + 1))) // (10 ** i)
            mp = ord(ms[i]) - 48
            if ip < mp:
                need_check = False
            elif need_check and ip > mp:
                return 0
            r += ip * (10 ** (int_len - 1 - i))
        if flag == 1:
            return r
        else:
            return -r


print(Solution().reverse(1234567890))

