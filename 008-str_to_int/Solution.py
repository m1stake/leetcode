
class Solution:

    int_max = 2**31 - 1
    int_min = -2**31

    int_min_s = '2147483648'
    int_max_s = '2147483647'

    def myAtoi(self, s: str) -> int:

        if len(s) == 0:
            return 0

        signal = 1
        nums = ''
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

        for _ in range(11):
            if '0' <= s[idx] <= '9':
                nums += s[idx]
                idx += 1
                if len(s) == idx:
                    break
            else:
                break

        if len(nums) == 0:
            return 0
        elif len(nums) > 10:
            if signal:
                return Solution.int_max
            else:
                return Solution.int_min
        elif len(nums) == 10:
            # 判断是否超出范围
            return self.overflow(nums, signal)
        else:
            return self.s_to_int(nums, signal)

    def overflow(self, nums, signal):
        if not signal:
            ns = Solution.int_min_s
        else:
            ns = Solution.int_max_s

        over = False
        for i in range(10):
            if nums[i] > ns[i]:
                over = True
                break
            elif nums[i] < ns[i]:
                over = False
                break

        if not over:
            return self.s_to_int(nums, signal)
        elif signal:
            return Solution.int_max
        else:
            return Solution.int_min

    def s_to_int(self, nums, signal):
        r = 0
        for c in nums:
            r = r * 10 + (ord(c) - 48)

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