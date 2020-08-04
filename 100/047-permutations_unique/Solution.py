from typing import List


class Solution:

    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return []

        if len(nums) == 1:
            return [nums]

        unique_set = set()
        r = []

        for i in range(len(nums)):

            if not nums[i] in unique_set:
                cut = nums[:]
                del cut[i]

                for x in self.permuteUnique(cut):
                    x.append(nums[i])
                    r.append(x)

                unique_set.add(nums[i])

        return r


print(
    Solution().permuteUnique([1,2,1]),
)
