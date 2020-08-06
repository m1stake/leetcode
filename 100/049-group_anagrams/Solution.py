from typing import List


class Solution:

    """
    {
        010101: [],
        101010: []
    }
    假设字符串内没有重复字符
    """

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        a_ord = 97

        m = {}

        for s in strs:
            s_bit = 0
            for c in s:
                s_bit |= 1 << (ord(c) - a_ord)

            if s_bit in m:
                m[s_bit].append(s)
            else:
                m[s_bit] = [s]

        r = []
        for k in m:
            r.append(m[k])

        return r


print(
    Solution().groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
)