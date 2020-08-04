from typing import List


class Solution:

    def permute(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return []

        if len(nums) == 1:
            return [nums]

        r = []

        for i in range(len(nums)):
            cut = nums[:i] + nums[i+1:]
            tr = list(map(lambda x: Solution.a(x, nums[i]), self.permute(cut)))
            r += tr

        return r

    @staticmethod
    def a(x, n):
        x.append(n)
        return x


print(
    Solution().permute([1,2,3]),
)
