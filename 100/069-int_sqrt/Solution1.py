import math

class Solution:

    def mySqrt(self, x: int) -> int:

        return self.bi_sqrt(0, x, x)

    def bi_sqrt(self, start, end, x):

        if start == end:
            return start

        mid = (start + end + 1) // 2

        mm = mid * mid
        mm1 = (mid + 1) * (mid + 1)

        if mm <= x < mm1:
            return mid
        elif mm < x:
            return self.bi_sqrt(mid, end, x)
        else:
            return self.bi_sqrt(0, mid, x)


print(
    Solution().mySqrt(0),
    Solution().mySqrt(1),
    Solution().mySqrt(2),
    Solution().mySqrt(3),
    Solution().mySqrt(4),
    Solution().mySqrt(5),
    Solution().mySqrt(8),
    Solution().mySqrt(10),
)



