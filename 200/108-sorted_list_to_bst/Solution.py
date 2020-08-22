from typing import List
from TreeNodeUtil import TreeNode


class Solution:

    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:

        if not nums:
            return None

        n_idx = len(nums) // 2
        node = TreeNode(nums[n_idx])

        node.left = self.sortedArrayToBST(nums[:n_idx])
        node.right = self.sortedArrayToBST(nums[n_idx+1:])

        return node


print(
    Solution().sortedArrayToBST([]),
    Solution().sortedArrayToBST([1]),
    Solution().sortedArrayToBST([1, 2, 3, 4]),
    Solution().sortedArrayToBST([1, 2, 3, 4, 5]),
    Solution().sortedArrayToBST([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]),
)
