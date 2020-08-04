from typing import List


class Solution:

    def longestCommonPrefix(self, strs: List[str]) -> str:

        same_prefix = ''

        if len(strs) == 0:
            return same_prefix
        elif len(strs) == 1:
            return strs[0]

        first_s = strs[0]
        rest_s = strs[1:]
        idx = 0
        while idx < len(first_s):

            for s in rest_s:
                if idx >= len(s) or (not s[idx] == first_s[idx]):
                    return same_prefix

            same_prefix += first_s[idx]
            idx += 1

        return same_prefix


print(
    Solution().longestCommonPrefix([]),
    Solution().longestCommonPrefix(['']),
    Solution().longestCommonPrefix(['', '']),
    Solution().longestCommonPrefix(['123', '12', '124']),
)