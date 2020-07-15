

class Solution:

    def isPalindrome(self, x: int) -> bool:

        if x < 0:
            return False

        r = 0
        tmp = x
        while tmp > 0:
            r = r * 10 + tmp % 10
            tmp //= 10

        return r == x


print(
    Solution().isPalindrome(121),
    Solution().isPalindrome(-121),
    Solution().isPalindrome(10),
    Solution().isPalindrome(-0),
    Solution().isPalindrome(10000021),
    0 is -0
)








