
class Solution:

    def isValid(self, s: str) -> bool:

        left = ['(', '[', '{']

        m = {
            ')': '(',
            ']': '[',
            '}': '{'
        }

        stack = []

        for c in s:
            if c in left:
                stack.append(c)
            elif (not stack) or (not stack.pop() == m[c]):
                return False

        return not stack


print(
    Solution().isValid('()'),
    Solution().isValid('()[]{}'),
    Solution().isValid('(]'),
    Solution().isValid('({)}'),
    Solution().isValid('}'),

)