from typing import List


class Solution:

    def permute(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return []

        if len(nums) == 1:
            return [nums]

        r = []

        for i in range(len(nums)):

            cut = nums[:]
            del cut[i]

            for x in self.permute(cut):
                x.append(nums[i])
                r.append(x)

        return r


print(
    Solution().permute([1,2,3]),
)
