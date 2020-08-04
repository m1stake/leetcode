

class Solution:

    def divide(self, dividend: int, divisor: int) -> int:

        if dividend == -2147483648 and divisor == -1:
            return 2147483647

        flag = not (dividend < 0) ^ (divisor < 0)

        dividend = abs(dividend)
        divisor = abs(divisor)

        quotient = self.divide0(dividend, divisor)

        return quotient if flag else -quotient

    def divide0(self, dividend, divisor):

        cd = divisor

        quotient = 0
        multiple = 1
        t = 0

        while True:

            t += cd

            if t <= dividend:
                quotient += multiple
            else:

                if multiple == 1:
                    return quotient
                else:
                    return quotient + self.divide0(dividend - (t - cd), divisor)

            multiple += multiple
            cd += cd


print(
    Solution().divide(0, 1),
    Solution().divide(1, 1),
    Solution().divide(1, 2),
    Solution().divide(2, 1),
    Solution().divide(0, -1),
    Solution().divide(1, -1),
    Solution().divide(-1, 2),
    Solution().divide(-2, 1),
    Solution().divide(-200, 10),
    Solution().divide(-2147483647, -1),
    Solution().divide(-2147483648, -1),

)
