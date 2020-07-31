from typing import List


class Solution:

    def searchRange(self, nums: List[int], target: int) -> List[int]:

        if not nums:
            return [-1, -1]

        return [
            self.searchRangeLeft(nums, target, 0, len(nums)),
            self.searchRangeRight(nums, target, 0, len(nums))
        ]

    def searchRangeLeft(self, nums: List[int], target, left, right) -> int:

        if right <= left:
            return -1
        elif right == left + 1:
            if nums[left] == target:
                return left
            else:
                return -1

        mid_idx = left + (right - left - 1) // 2
        mid = nums[mid_idx]

        if mid < target:
            return self.searchRangeLeft(nums, target, mid_idx + 1, right)
        else:
            return self.searchRangeLeft(nums, target, left, mid_idx + 1)

    def searchRangeRight(self, nums: List[int], target, left, right) -> int:

        if right <= left:
            return -1
        elif right == left + 1:
            if nums[left] == target:
                return left
            else:
                return -1

        mid_idx = left + (right - left) // 2
        mid = nums[mid_idx]

        if mid > target:
            return self.searchRangeRight(nums, target, left, mid_idx)
        else:
            return self.searchRangeRight(nums, target, mid_idx, right)


print(
    Solution().searchRange([], 1),
    Solution().searchRange([1], 1),
    Solution().searchRange([1, 1], 1),
    Solution().searchRange([1, 1, 2], 1),
    Solution().searchRange([1, 2, 2], 2),
    Solution().searchRange([1, 2, 2], 3),
    Solution().searchRange([1, 2, 3, 4, 5, 5, 6, 7], 5),
    Solution().searchRange([1, 2, 3, 4, 5, 5, 6, 7, 7], 7),
)

