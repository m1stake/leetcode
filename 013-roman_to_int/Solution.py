
class Solution:

    m = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000

    }

    def romanToInt(self, s: str) -> int:

        len_s = len(s)
        i = 0
        r = 0
        while i < len_s:
            cur_v = Solution.m[s[i]]
            if (i < len_s - 1) and cur_v < Solution.m[s[i + 1]]:
                r -= cur_v
            else:
                r += cur_v

            i += 1
        return r


print(
    Solution().romanToInt('III'),
    Solution().romanToInt('IV'),
    Solution().romanToInt('IX'),
    Solution().romanToInt('LVIII'),
    Solution().romanToInt('MCMXCIV')
)