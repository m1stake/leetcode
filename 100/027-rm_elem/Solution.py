from typing import List


class Solution:

    def removeElement(self, nums: List[int], val: int) -> int:

        tail_idx = 0

        for i in range(len(nums)):
            c = nums[i]
            if not c == val:
                if not i == tail_idx:
                    nums[tail_idx] = c

                tail_idx += 1

        print(nums)
        return tail_idx


print(
    Solution().removeElement([], 0),
    Solution().removeElement([1], 0),
    Solution().removeElement([0], 0),
    Solution().removeElement([0, 0], 0),
    Solution().removeElement([1, 0, 0], 0),
    Solution().removeElement([1, 0, 0, 1], 0),


)


