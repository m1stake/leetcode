from typing import List


class Solution:

    """
    空间 n/32
    """

    def firstMissingPositive(self, nums: List[int]) -> int:

        b = 0

        for i in nums:
            if 0 < i <= len(nums):
                b |= 1 << i

        offset = 1
        while True:
            t = 1 << offset
            if not (b & t) == t:
                return offset
            offset += 1


print(
    Solution().firstMissingPositive([1, 2, 0]),
    Solution().firstMissingPositive([3, 4, -1, 1]),
    Solution().firstMissingPositive([7, 8, 9, 11, 12]),
    Solution().firstMissingPositive([12000000, 12000000, 12000000, 12000000, 12000000]),
)
















