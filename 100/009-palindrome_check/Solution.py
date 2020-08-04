

class Solution:

    def isPalindrome(self, x: int) -> bool:

        if x < 0:
            return False

        int_len = self.int_len(x)

        for i in range(int_len // 2):
            if not self.int_at(i, x) == self.int_at(int_len - 1 - i, x):
                return False
        return True

    def int_len(self, x):
        int_len = 1
        while True:
            if x < 10 ** int_len:
                return int_len
            else:
                int_len += 1

    def int_at(self, i, x):
        return (x % (10 ** (i + 1))) // (10 ** i)


print(
    Solution().isPalindrome(121),
    Solution().isPalindrome(-121),
    Solution().isPalindrome(10),
    Solution().isPalindrome(-0),
    Solution().isPalindrome(10000021),
    0 is -0
)








