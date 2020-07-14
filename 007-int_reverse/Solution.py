

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

        rsx = self.to_reverse_str(x)
        if self.overflow_check(flag, rsx):
            return 0
        else:
            return self.to_int(flag, rsx)

    def overflow_check(self, flag, rsx):
        if len(rsx) == Solution.OVERFLOW_LEN:
            if flag == 1:
                ms = Solution.MAX_INT_S
            else:
                ms = Solution.MIN_INT_S
            for ri in range(Solution.OVERFLOW_LEN):
                if rsx[ri] < ms[ri]:
                    return False
                elif rsx[ri] > ms[ri]:
                    return True
                else:
                    continue
            return True
        else:
            return False

    def to_reverse_str(self, x):
        int_len = self.int_len(x)
        s = ''
        for i in range(int_len):
            s += chr(((x % (10 ** (i + 1))) // (10 ** i)) + 48)
        return s

    def int_len(self, x):
        for i in range(Solution.OVERFLOW_LEN):
            if x <= Solution.SIZE_TABLE[i]:
                return i + 1
        raise Exception("int size overflow")

    def to_int(self, flag, rsx):
        r = 0
        for i in range(len(rsx)):
            r += (ord(rsx[len(rsx) - i - 1]) - 48) * (10 ** i)
        if flag == 1:
            return r
        else:
            return -r


