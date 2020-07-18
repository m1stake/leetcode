
class Solution:

    int_max = 2**31 - 1
    int_min = -2**31

    int_min_s = '2147483648'
    int_max_s = '2147483647'

    max_nine = 214748364

    def myAtoi(self, s: str) -> int:

        if len(s) == 0:
            return 0

        signal = 1
        idx = 0

        # 去掉空格
        while idx < len(s):
            if s[idx] == ' ':
                idx += 1
            else:
                break

        # 判断符号
        if len(s) == idx:
            return 0

        if s[idx] in ['+', '-']:
            signal = 1 if s[idx] == '+' else 0
            idx += 1

        # 扫描数字
        if len(s) == idx:
            return 0

        # 去掉前置的0
        while idx < len(s):
            if s[idx] == '0':
                idx += 1
            else:
                break

        if len(s) == idx:
            return 0

        r = 0

        for i in range(11):
            if '0' <= s[idx] <= '9':

                if i == 10:
                    if signal:
                        return Solution.int_max
                    else:
                        return Solution.int_min

                nc = ord(s[idx]) - 48

                if i == 9:
                    if r > Solution.max_nine:
                        if signal:
                            return Solution.int_max
                        else:
                            return Solution.int_min
                    elif r == Solution.max_nine:
                        if signal and nc >= 7:
                            return Solution.int_max
                        elif (not signal) and nc >= 8:
                            return Solution.int_min

                r = r * 10 + nc

                idx += 1
                if len(s) == idx:
                    break
            else:
                break

        if signal:
            return r
        else:
            return -r


print(
    Solution().myAtoi(''),
    Solution().myAtoi('-'),
    Solution().myAtoi('+'),
    Solution().myAtoi(' -'),
    Solution().myAtoi(' +'),
    Solution().myAtoi(' +1'),
    Solution().myAtoi(' +a'),
    Solution().myAtoi(' -1'),
    Solution().myAtoi(' -a'),
    Solution().myAtoi(' +11111111111111111111'),
    Solution().myAtoi(' -11111111111111111111'),
    Solution().myAtoi(' -2147483649'),
    Solution().myAtoi(' 2147483649'),
    Solution().myAtoi(' 214748364a'),
)