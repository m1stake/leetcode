from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:

        if k == 0:
            return []

        ns = [x + 1 for x in range(n)]

        return self.combine0(ns, k)

    def combine0(self, ns, k):
        if k == 1:
            return [[x] for x in ns]

        r = []
        for i in range(len(ns) - k + 1):

            for c in self.combine0(ns[i+1:len(ns)], k-1):
                r.append([ns[i]] + c)

        return r


print(
    Solution().combine(3, 1),
    Solution().combine(4, 2),
    Solution().combine(3, 3),

)
