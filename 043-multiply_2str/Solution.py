

class Solution:

    """
    太慢 280ms
    """

    def multiply(self, num1: str, num2: str) -> str:

        r = 0

        for i in range(len(num1)):
            for j in range(len(num2)):
                c1 = int(num1[len(num1) - i - 1])
                c2 = int(num2[len(num2) - j - 1])
                r += c1 * c2 * (10 ** (i + j))

        return str(r)


print(
    Solution().multiply('0', '123'),
    Solution().multiply('123', '123'),
    Solution().multiply('123', '456'),
    Solution().multiply('10' * 50, '20' * 50),
)



