from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:

        r = 0

        for n in nums:
            r ^= n

        return r


print(
    Solution().singleNumber([1,2,3,3,1])
)