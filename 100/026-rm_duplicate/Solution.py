from typing import List


class Solution:

    """
    用时过长
    """

    def removeDuplicates(self, nums: List[int]) -> int:

        if not nums:
            return 0

        # 删掉几个
        # 移动几个

        duplicate_count = 1

        mv_count = 1

        cs = nums[-1]
        len_nums = len(nums)

        for i in range(len(nums) - 1):
            idx = len_nums - 2 - i
            c = nums[idx]
            if c == cs:
                duplicate_count += 1
            else:

                if duplicate_count > 1:

                    s_idx = idx + duplicate_count
                    for j in range(mv_count):
                        nums[idx + j + 1] = nums[s_idx + j]

                    duplicate_count = 1

                mv_count += 1
                cs = c

        # 处理开头重复
        if duplicate_count > 1:

            s_idx = duplicate_count - 1
            for j in range(mv_count):
                nums[j] = nums[s_idx + j]

        print(nums, end=', ')
        return mv_count


print(Solution().removeDuplicates([1]))
print(Solution().removeDuplicates([1,1]))
print(    Solution().removeDuplicates([2,1,1,1,2]))
print(    Solution().removeDuplicates([1,1,1,2]))
print(    Solution().removeDuplicates([2,1,1,1]))


