

class Solution:

    def multiply(self, num1: str, num2: str) -> str:

        m = [0 for _ in range(len(num1) * len(num2) + 2)]

        for i in range(len(num1)):
            for j in range(len(num2)):
                c1 = ord(num1[len(num1) - i - 1]) - 48
                c2 = ord(num2[len(num2) - j - 1]) - 48

                mc = m[i + j]
                v = c1 * c2 + mc

                m[i + j] = v % 10
                m[i + j + 1] += v // 10

        pre_zero = True
        r = ''
        for x in range(len(m) - 1, -1, -1):
            if not m[x] == 0:
                r += chr(m[x] + 48)
                pre_zero = False
            elif not pre_zero:
                r += chr(m[x] + 48)

        if r:
            return r
        else:
            return '0'


print(
    Solution().multiply('0', '123'),
    Solution().multiply('49', '49'),
    Solution().multiply('123', '123'),
    Solution().multiply('123', '456'),
    Solution().multiply('10' * 50, '20' * 50),

)



