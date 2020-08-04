from typing import List


class Solution:

    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # 找到n位之后比n位大的数，置换
        sorted_highest_idx_map = []

        for i in range(len(nums)):
            c_idx = len(nums) - 1 - i
            cn = nums[c_idx]
            for hp in sorted_highest_idx_map:
                hn = hp[0]
                hi = hp[1]
                if hn > cn:

                    # 大数换到当前位置
                    tmp = nums[c_idx]
                    nums[c_idx] = nums[hi]

                    # 之后的数和被替换的数，从小到大排列，填回数组中
                    tmp_filled = False
                    for n, _ in sorted_highest_idx_map:
                        if n <= tmp or tmp_filled:
                            nums[c_idx + 1] = n
                        else:
                            nums[c_idx + 1] = tmp
                            tmp_filled = True

                        c_idx += 1

                    print(nums)
                    return
                elif hn == cn:
                    hp[1] = c_idx

            sorted_highest_idx_map.append([cn, c_idx])

        # 翻转nums
        for i in range(len(nums) // 2):
            tmp = nums[i]
            nums[i] = nums[len(nums) - 1 - i]
            nums[len(nums) - 1 - i] = tmp

        print(nums)


print(
    Solution().nextPermutation([]),
    Solution().nextPermutation([1]),
    Solution().nextPermutation([1, 1]),
    Solution().nextPermutation([1, 2, 3]),
    Solution().nextPermutation([1, 3, 2]),
    Solution().nextPermutation([1, 1, 2, 3]),
    Solution().nextPermutation([1, 2, 2, 3]),
    Solution().nextPermutation([1, 2, 2, 3, 3]),
    Solution().nextPermutation([2, 3, 1]),
    Solution().nextPermutation([3, 2, 1]),

)

