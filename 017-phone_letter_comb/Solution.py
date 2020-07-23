from typing import List


class Solution:

    m = {
        '0': [],
        '1': [],
        '2': ['a', 'b', 'c'],
        '3': ['d', 'e', 'f'],
        '4': ['g', 'h', 'i'],
        '5': ['j', 'k', 'l'],
        '6': ['m', 'n', 'o'],
        '7': ['p', 'q', 'r', 's'],
        '8': ['t', 'u', 'v'],
        '9': ['w', 'x', 'y', 'z']
    }


    def letterCombinations(self, digits: str) -> List[str]:

        rs = []

        if digits:

            d = digits[0]
            for letter in Solution.m[d]:

                tail = self.letterCombinations(digits[1:])
                if tail:
                    for lc in tail:
                        rs.append(letter + lc)
                else:
                    rs.append(letter)

        else:
            return []

        return rs


print(
    Solution().letterCombinations(''),
    Solution().letterCombinations('0'),
    Solution().letterCombinations('1'),
    Solution().letterCombinations('01'),
    Solution().letterCombinations('234'),
    Solution().letterCombinations('1234'),
    Solution().letterCombinations('2134'),
    Solution().letterCombinations('2341'),
)


