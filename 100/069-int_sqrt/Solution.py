class Solution:
    def mySqrt(self, x: int) -> int:

        for i in range(x // 2 + 3):
            if i * i > x:
                return i - 1


