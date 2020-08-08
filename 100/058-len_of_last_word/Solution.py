

class Solution:

    def lengthOfLastWord(self, s: str) -> int:

        new_end = True
        count = 0

        for c in s:

            if not c == ' ':
                if new_end:
                    count = 1
                    new_end = False
                else:
                    count += 1
            else:
                new_end = True

        return count


print(
    Solution().lengthOfLastWord(''),
    Solution().lengthOfLastWord(' '),
    Solution().lengthOfLastWord('abc'),
    Solution().lengthOfLastWord(' abc'),
    Solution().lengthOfLastWord(' abc '),
    Solution().lengthOfLastWord('ab c'),
    Solution().lengthOfLastWord(' ab c'),
    Solution().lengthOfLastWord(' ab c '),
    Solution().lengthOfLastWord('ab c '),
)

