from typing import List


class Solution:

    def generateParenthesis(self, n: int) -> List[str]:

        if n == 0:
            return []

        left_rest = n
        right_rest = n

        return self.generateParenthesis0(left_rest, right_rest, '')

    def generateParenthesis0(self, left_rest, right_rest, head: str):

        if right_rest == 0:
            return [head]

        if left_rest == right_rest:
            return self.generateParenthesis0(left_rest - 1, right_rest, head + '(')
        elif left_rest > 0:
            return \
                self.generateParenthesis0(left_rest - 1, right_rest, head + '(') \
                + self.generateParenthesis0(left_rest, right_rest - 1, head + ')')
        else:
            return self.generateParenthesis0(left_rest, right_rest - 1, head + ')')


print(
    Solution().generateParenthesis(0),
    Solution().generateParenthesis(1),
    Solution().generateParenthesis(2),
    Solution().generateParenthesis(3),

)
