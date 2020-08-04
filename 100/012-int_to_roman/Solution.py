
class Solution:

    ones = ['I', 'X', 'C', 'M']
    fives = ['V', 'L', 'D']

    """
    I 可以放在 V (5) 和 X (10) 的左边，来表示 4 和 9。
    X 可以放在 L (50) 和 C (100) 的左边，来表示 40 和 90。 
    C 可以放在 D (500) 和 M (1000) 的左边，来表示 400 和 900。
    
    0   1   2   3   4   5   6   7   8       9   
        i   ii  iii iv  v   vi  vii viii    ix
    
    
    """

    def intToRoman(self, num: int) -> str:

        r = ''
        position = 0
        while num > 0:
            nc = num % 10
            num //= 10

            r = self.intToRoman0(nc, position) + r

            position += 1

        return r

    def intToRoman0(self, nc, position):

        if 0 <= nc <= 3:
            return Solution.ones[position] * nc
        elif nc == 4:
            return Solution.ones[position] + Solution.fives[position]
        elif 5 <= nc <= 8:
            return Solution.fives[position] + Solution.ones[position] * (nc - 5)
        else:
            return Solution.ones[position] + Solution.ones[position + 1]


print(
    Solution().intToRoman(3),
    Solution().intToRoman(4),
    Solution().intToRoman(9),
    Solution().intToRoman(58),
    Solution().intToRoman(1994),
)
