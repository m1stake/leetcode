

class Solution:

    def isPalindrome(self, x: int) -> bool:

        if x < 0:
            return False

        r = 0
        idx = 0
        len_check = 10
        while True:

            r = r * 10 + (x % (10 ** (idx + 1))) // (10 ** idx)

            if x < len_check:
                return r == x
            else:
                len_check *= 10
                idx += 1

print(
    Solution().isPalindrome(121),
    Solution().isPalindrome(-121),
    Solution().isPalindrome(10),
    Solution().isPalindrome(-0),
    Solution().isPalindrome(10000021),
    0 is -0
)








