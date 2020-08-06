from typing import List


class Solution:

    """
    {
        '0,1,0,2': [],
        '1,0,1,3': []
    }
    """

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        a_ord = 97

        m = {}

        for s in strs:
            k = [0] * 26
            for c in s:
                idx = (ord(c) - a_ord)
                k[idx] += 1

            sk = str(k)
            if sk in m:
                m[sk].append(s)
            else:
                m[sk] = [s]

        r = []
        for mk in m:
            r.append(m[mk])

        return r


print(
    Solution().groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]),
    Solution().groupAnagrams(['aac', 'cca', 'cac', 'cba']),
)