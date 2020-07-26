

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:

        if not needle:
            return 0

        for i in range(len(haystack) - len(needle) + 1):
            if haystack[i] == needle[0]:
                match = True
                for j in range(len(needle)):
                    if (i + j >= len(haystack)) or (not haystack[i + j] == needle[j]):
                        match = False
                        break

                if match:
                    return i

        return -1


print(
    Solution().strStr('aabc', 'abc'),
    Solution().strStr('abc', 'aabc')

)